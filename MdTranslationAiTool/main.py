"""
بىلىك تەرجىمە قۇرالى v1.0
ۋېب ئاساسىدا: http://127.0.0.1:5173
"""
import os
import json
import queue
import threading
import webbrowser
import time
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from datetime import datetime
from flask import Flask, render_template, Response, request, jsonify

from translators import TRANSLATORS
from translators.base import FatalTranslationError
from processors import get_processor, PROCESSORS
from utils.cache import TranslationCache
from utils.glossary import Glossary
from utils.config import Config
from utils.logger_util import get_logger

app = Flask(__name__)
app.secret_key = "mdtranslation_2024"

config   = Config()
cache    = TranslationCache()
glossary = Glossary()

jobs:       dict[str, queue.Queue]     = {}
stop_flags: dict[str, threading.Event] = {}

_folder_event  = threading.Event()
_folder_result = {"path": ""}

TARGET_LANGS = {
    "ئۇيغۇرچە": "Uyghur",
    "تۈركچە":   "Turkish",
    "قازاقچە":  "Kazakh",
    "ئۆزبېكچە": "Uzbek",
    "ئەرەبچە":  "Arabic",
    "پارسچە":   "Persian",
    "روسچە":    "Russian",
    "ئەنگلىزچە":"English",
    "خىتايچە":  "Chinese",
}

SUPPORTED_EXTS = list(PROCESSORS.keys())


# ================================================================ #
#                             Routes                                #
# ================================================================ #

@app.route("/")
def index():
    return render_template("index.html",
        providers=list(TRANSLATORS.keys()),
        target_langs=list(TARGET_LANGS.keys()),
    )


@app.route("/api/config")
def get_config():
    return jsonify({
        "chunk_size":    config.get("chunk_size", 3000),
        "last_provider": config.get("last_provider", list(TRANSLATORS.keys())[0]),
        "last_model":    config.get("last_model", ""),
        "last_lang":     config.get("last_lang", "ئۇيغۇرچە"),
        "cache_size":    cache.size(),
    })


@app.route("/api/models/<provider>")
def get_models(provider):
    cls = TRANSLATORS.get(provider)
    if not cls:
        return jsonify({"models": [], "default": ""})
    return jsonify({
        "models":  cls.get_available_models(),
        "default": cls.get_default_model(),
    })


@app.route("/api/keys")
def get_keys():
    return jsonify({p: bool(config.get_api_key(p)) for p in TRANSLATORS})


@app.route("/api/keys", methods=["POST"])
def save_key():
    data     = request.json
    provider = data.get("provider", "")
    key      = data.get("key", "").strip()
    if provider in TRANSLATORS and key:
        config.set_api_key(provider, key)
        return jsonify({"ok": True})
    return jsonify({"ok": False, "error": "يارامسىز تەرجىمان ياكى بوش كۇنۇپكا"})


@app.route("/api/test-connection", methods=["POST"])
def test_connection():
    data     = request.json
    provider = data.get("provider", "")
    key      = data.get("key", "").strip() or config.get_api_key(provider)
    if not key:
        return jsonify({"ok": False, "error": "API كۇنۇپكا يوق"})
    try:
        translator = TRANSLATORS[provider](api_key=key)
        ok = translator.test_connection()
        return jsonify({"ok": ok})
    except FatalTranslationError as e:
        return jsonify({"ok": False, "error": str(e), "fatal": True})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


@app.route("/api/browse-folder", methods=["POST"])
def browse_folder():
    """Windows PowerShell ئارقىلىق فولدېر تاللايدۇ — ئەڭ ئىشەنچلىك ئۇسۇل"""
    _folder_result["path"]  = ""
    _folder_result["ready"] = False
    _folder_event.set()          # main thread غا سىگنال
    return jsonify({"triggered": True})


@app.route("/api/folder-result")
def folder_result_poll():
    """Browser polling ئارقىلىق نەتىجىنى ئالىدۇ"""
    if _folder_result.get("ready"):
        path = _folder_result.get("path", "")
        req_exists = bool(path) and (Path(path) / "تەلەپ.txt").exists()
        return jsonify({"done": True, "path": path, "req_exists": req_exists})
    return jsonify({"done": False})


@app.route("/api/dry-run", methods=["POST"])
def dry_run():
    data      = request.json
    folder    = data.get("folder", "")
    max_chars = int(data.get("chunk_size", 3000))
    if not folder or not os.path.isdir(folder):
        return jsonify({"error": "فولدېر يوق"})
    files   = _collect_files(folder)
    results = []
    total   = 0
    for fpath in files:
        try:
            chunks   = get_processor(str(fpath)).split_chunks(max_chars)
            refs     = sum(1 for c in chunks if c.is_reference)
            trans    = len(chunks) - refs
            total   += trans
            results.append({"name": fpath.name, "translate": trans, "reference": refs})
        except Exception as e:
            results.append({"name": fpath.name, "error": str(e)})
    return jsonify({"files": results, "total_chunks": total, "total_files": len(files)})


@app.route("/api/translate", methods=["POST"])
def start_translation():
    data         = request.json
    folder       = data.get("folder", "")
    provider     = data.get("provider", "")
    model        = data.get("model", "")
    lang         = data.get("lang", "ئۇيغۇرچە")
    resume       = data.get("resume", True)
    use_cache    = data.get("use_cache", True)
    max_chars    = int(data.get("chunk_size", 3000))
    preview_only = data.get("preview_only", False)

    if not folder or not os.path.isdir(folder):
        return jsonify({"error": "فولدېر تاپىلمىدى"})
    key = config.get_api_key(provider)
    if not key:
        return jsonify({"error": f"{provider} ئۈچۈن API كۇنۇپكا يوق"})

    job_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    q      = queue.Queue()
    stop   = threading.Event()
    jobs[job_id]       = q
    stop_flags[job_id] = stop

    config.set("last_provider", provider)
    config.set("last_model", model)
    config.set("last_lang", lang)

    def run():
        try:
            translator   = TRANSLATORS[provider](api_key=key, model=model)
            target_lang  = TARGET_LANGS.get(lang, "Uyghur")
            sys_prompt   = _build_system_prompt(folder, target_lang)
            logger       = get_logger(job_id)
            files        = _collect_files(folder)
            if preview_only:
                files = files[:1]
            total = len(files)
            q.put({"type": "start", "total_files": total})
            out_root = Path(folder).parent / f"{Path(folder).name}-ug"
            q.put({"type": "info", "msg": f"چىقىرىش فولدېرى: {out_root}"})

            for fi, fpath in enumerate(files):
                if stop.is_set():
                    q.put({"type": "stopped"})
                    break

                out_path = _output_path(fpath, Path(folder))
                if resume and not preview_only and out_path.exists():
                    q.put({"type": "skipped", "file": fpath.name, "fi": fi + 1, "total": total})
                    continue

                q.put({"type": "file_start", "file": fpath.name, "fi": fi + 1, "total": total})
                logger.info(f"Translating: {fpath}")

                try:
                    chunks = get_processor(str(fpath)).split_chunks(max_chars)
                except Exception as e:
                    q.put({"type": "error", "msg": f"{fpath.name}: {e}"})
                    continue

                parts        = []
                total_chunks = len(chunks)

                for ci, chunk in enumerate(chunks):
                    if stop.is_set():
                        break
                    q.put({"type": "chunk", "ci": ci + 1, "total": total_chunks})

                    if chunk.is_reference:
                        parts.append(chunk.text)
                        q.put({"type": "chunk_done", "ci": ci + 1, "ref": True})
                        continue

                    cached = cache.get(provider, model, chunk.text) if use_cache else None
                    if cached:
                        parts.append(cached)
                        q.put({"type": "chunk_done", "ci": ci + 1, "cached": True})
                    else:
                        try:
                            result = translator.translate(chunk.text, sys_prompt)
                            parts.append(result)
                            if use_cache:
                                cache.set(provider, model, chunk.text, result)
                            q.put({"type": "chunk_done", "ci": ci + 1, "cached": False})
                            logger.info(f"  chunk {ci+1}/{total_chunks}")
                        except FatalTranslationError as e:
                            q.put({"type": "fatal", "msg": str(e)})
                            logger.error(f"Fatal: {e}")
                            stop.set()
                            break
                        except Exception as e:
                            parts.append(chunk.text)
                            q.put({"type": "error", "msg": f"بۆلەك {ci+1}: {e}"})
                            logger.error(f"  chunk {ci+1} error: {e}")

                if stop.is_set():
                    break

                if preview_only:
                    orig = chunks[0].text if chunks else ""
                    q.put({"type": "preview", "original": orig,
                           "translated": "\n\n".join(parts[:1])})
                else:
                    out_path.write_text("\n\n".join(parts), encoding="utf-8")
                    q.put({"type": "file_done", "file": fpath.name, "path": str(out_path)})
                    logger.info(f"Saved: {out_path}")

            if not stop.is_set():
                q.put({"type": "done"})
            logger.info("Session complete")
        except Exception as e:
            q.put({"type": "fatal", "msg": str(e)})
        finally:
            q.put({"type": "end"})

    threading.Thread(target=run, daemon=True).start()
    return jsonify({"job_id": job_id})


@app.route("/api/progress/<job_id>")
def progress_stream(job_id):
    def generate():
        q = jobs.get(job_id)
        if not q:
            yield f"data: {json.dumps({'type':'error','msg':'job not found'})}\n\n"
            return
        while True:
            try:
                msg = q.get(timeout=30)
                yield f"data: {json.dumps(msg, ensure_ascii=False)}\n\n"
                if msg.get("type") in ("end", "fatal", "stopped"):
                    jobs.pop(job_id, None)
                    stop_flags.pop(job_id, None)
                    break
            except queue.Empty:
                yield "data: {\"type\":\"heartbeat\"}\n\n"
    return Response(generate(), mimetype="text/event-stream",
                    headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


@app.route("/api/stop/<job_id>", methods=["POST"])
def stop_job(job_id):
    flag = stop_flags.get(job_id)
    if flag:
        flag.set()
    return jsonify({"ok": True})


@app.route("/api/glossary")
def get_glossary():
    return jsonify(glossary.all())

@app.route("/api/glossary", methods=["POST"])
def add_glossary():
    d = request.json
    src = d.get("source", "").strip()
    tgt = d.get("target", "").strip()
    if src and tgt:
        glossary.add(src, tgt)
        return jsonify({"ok": True})
    return jsonify({"ok": False})

@app.route("/api/glossary/<path:term>", methods=["DELETE"])
def del_glossary(term):
    glossary.remove(term)
    return jsonify({"ok": True})

@app.route("/api/cache/info")
def cache_info_route():
    return jsonify({"size": cache.size()})

@app.route("/api/cache/clear", methods=["POST"])
def cache_clear():
    cache.clear()
    return jsonify({"ok": True, "size": 0})

@app.route("/api/settings", methods=["POST"])
def save_settings():
    for k, v in (request.json or {}).items():
        config.set(k, v)
    return jsonify({"ok": True})


# ================================================================ #
#                           Helpers                                 #
# ================================================================ #

def _collect_files(folder: str) -> list[Path]:
    files = []
    for root, _, fnames in os.walk(folder):
        for fname in sorted(fnames):
            if Path(fname).suffix.lower() in SUPPORTED_EXTS:
                files.append(Path(root) / fname)
    return files


def _output_path(src: Path, src_folder: Path) -> Path:
    out = src_folder.parent / f"{src_folder.name}-ug" / src.relative_to(src_folder)
    out.parent.mkdir(parents=True, exist_ok=True)
    return out


def _build_system_prompt(folder: str, target_lang: str) -> str:
    req_text = ""
    req_path = Path(folder) / "تەلەپ.txt"
    if req_path.exists():
        try:
            import chardet
            raw = req_path.read_bytes()
            req_text = raw.decode(chardet.detect(raw)["encoding"] or "utf-8").strip()
        except Exception:
            pass

    prompt = f"""You are a professional translator. Translate the content into {target_lang}.

CRITICAL RULES — follow without exception:
1. Translate EVERY word completely. DO NOT shorten, summarize, or omit anything.
2. Preserve ALL markdown: headers, bold, italic, lists, tables, code blocks.
3. Keep ALL links as-is: [text](url) — only translate display text, never the URL.
4. Keep ALL images: ![alt](url) — only translate alt text if needed.
5. Keep ALL code blocks exactly as-is.
6. References, footnotes, citations — keep exactly as original.
7. Output ONLY the translated text. No extra comments."""

    if req_text:
        prompt += f"\n\nTRANSLATION REQUIREMENTS (from تەلەپ.txt):\n{req_text}"
    gloss = glossary.to_prompt_block()
    if gloss:
        prompt += f"\n\n{gloss}"
    return prompt


# ================================================================ #
#                           Entry Point                             #
# ================================================================ #

def run_flask(port: int):
    app.run(host="127.0.0.1", port=port, debug=False,
            use_reloader=False, threaded=True)


def _open_folder_dialog() -> str:
    """Windows PowerShell ئارقىلىق فولدېر تاللايدۇ — ئالدىدا كۆرۈنىدۇ"""
    try:
        import subprocess
        ps = (
            "Add-Type -AssemblyName System.Windows.Forms; "
            "$d = New-Object System.Windows.Forms.FolderBrowserDialog; "
            "$d.Description = 'Bilik - Terjime qilinadigan folderni talliyang'; "
            "$d.ShowNewFolderButton = $false; "
            "$null = $d.ShowDialog(); "
            "Write-Output $d.SelectedPath"
        )
        r = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps],
            capture_output=True, text=True, timeout=120
        )
        return (r.stdout or "").strip()
    except Exception:
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
            path = filedialog.askdirectory(parent=root, title="فولدېر تاللاڭ")
            root.destroy()
            return path or ""
        except Exception:
            return ""


def main():
    port = 5173

    flask_thread = threading.Thread(target=run_flask, args=(port,), daemon=True)
    flask_thread.start()

    time.sleep(0.8)
    webbrowser.open(f"http://127.0.0.1:{port}")

    print("[Bilik] http://127.0.0.1:5173 — qural hazir")
    # ئاساسىي تىزما: فولدېر تاللاش سىگنالىنى تىڭلا
    while True:
        _folder_event.wait()
        _folder_event.clear()
        path = _open_folder_dialog()
        _folder_result["path"]  = path
        _folder_result["ready"] = True


if __name__ == "__main__":
    main()
