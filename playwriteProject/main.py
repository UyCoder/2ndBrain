"""
Bilik AI Studio Terjime Qurali
-------------------------------
Tallanğan folderdiki .md / .txt / .pdf fichlarni
Google AI Studio arqiliq Uyghur tiligha tercime qilip
natijisini  <folder>/terjime_natijisi/  ichige saqlaydu.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox
    HAS_TK = True
except ImportError:
    HAS_TK = False

from file_processor import collect_files, read_file, split_chunks
from translator import AIStudioTranslator


# ── folder selection ──────────────────────────────────────────────────────────

def pick_folder() -> str:
    if HAS_TK:
        root = tk.Tk()
        root.withdraw()
        folder = filedialog.askdirectory(
            title="تەرجىمە قىلىنىدىغان فولدېرنى تاللاڭ"
        )
        root.destroy()
        return folder or ""
    return input("Tercime qilinadigan folder yolini kiriting: ").strip()


# ── accounts ──────────────────────────────────────────────────────────────────

def load_accounts() -> list:
    load_dotenv()
    accounts = []
    i = 1
    while True:
        email = os.getenv(f"GOOGLE_ACCOUNT_{i}_EMAIL")
        pwd   = os.getenv(f"GOOGLE_ACCOUNT_{i}_PASSWORD")
        if not email:
            break
        accounts.append({"email": email.strip(), "password": (pwd or "").strip()})
        i += 1
    return accounts


# ── output ────────────────────────────────────────────────────────────────────

def save_result(src: Path, translation: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / (src.stem + "_uyghur.md")
    content  = f"# {src.stem}\n\n{translation}"
    out_path.write_text(content, encoding="utf-8")
    return out_path


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    print()
    print("=" * 54)
    print("    Bilik AI Studio Terjime Qurali  v1.0")
    print("=" * 54)

    # 1. folder
    folder = pick_folder()
    if not folder:
        print("[INFO] Folder tallanmidi. Chiqildi.")
        return

    folder_path = Path(folder)
    out_dir     = folder_path / "terjime_natijisi"

    # 2. accounts
    accounts = load_accounts()
    if not accounts:
        msg = (
            ".env fichida Google hisab tapilmidi!\n"
            ".env.example ni korep .env ni teyerleng."
        )
        print(f"[ERROR] {msg}")
        if HAS_TK:
            messagebox.showerror("Xata", msg)
        sys.exit(1)

    # 3. collect files
    files = collect_files(str(folder_path))
    if not files:
        print("[INFO] MD, TXT yaki PDF fich tapilmidi.")
        return

    print(f"\n  Fichlar  : {len(files)}")
    print(f"  Hisablar : {len(accounts)}")
    print(f"  Natije   : {out_dir}")
    print()

    # 4. translate
    script_dir = Path(__file__).parent
    translator = AIStudioTranslator(
        accounts,
        profiles_dir=script_dir / "profiles",
    )

    total_ok   = 0
    total_fail = 0

    try:
        for i, fpath in enumerate(files, 1):
            out_path = out_dir / (fpath.stem + "_uyghur.md")

            # skip already-translated
            if out_path.exists():
                print(f"[{i}/{len(files)}] OTUP KETILDI (mewjut): {fpath.name}")
                continue

            print(f"[{i}/{len(files)}] {fpath.name}")

            text = read_file(fpath)
            if not text.strip():
                print("  Bosh fich — otup ketildi.")
                continue

            chunks = split_chunks(text)
            print(f"  {len(chunks)} bolek")

            parts = []
            chunk_ok = 0
            for j, chunk in enumerate(chunks, 1):
                print(f"  Bolek {j}/{len(chunks)} ...", end=" ", flush=True)
                result = translator.translate(chunk)
                if result:
                    print("OK")
                    parts.append(result)
                    chunk_ok += 1
                else:
                    print("MAGAZLIDI — esliy metin saqlandi")
                    parts.append(chunk)

            translation = "\n\n".join(parts)
            saved = save_result(fpath, translation, out_dir)
            print(f"  Saqlandi : {saved.name}  ({chunk_ok}/{len(chunks)} bolek tercime boldi)")

            if chunk_ok == len(chunks):
                total_ok += 1
            else:
                total_fail += 1

    except KeyboardInterrupt:
        print("\n[INFO] Toqtatildi.")
    finally:
        translator.close()

    print()
    print("=" * 54)
    print(f"  Tamam!  {total_ok} fich to'liq, {total_fail} fich qisman.")
    print(f"  Natijiler: {out_dir}")
    print("=" * 54)
    print()


if __name__ == "__main__":
    main()
