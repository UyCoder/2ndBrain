"""
Google AI Studio — Uyghur translation via CDP (Chrome DevTools Protocol).

Chrome is launched as a NORMAL browser (not via Playwright),
so Google cannot detect automation.  Playwright then connects
to the already-running Chrome over CDP and only operates on
the AI Studio page (no login automation needed).
"""

import os
import subprocess
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

# ── constants ─────────────────────────────────────────────────────────────────

_CDP_PORT   = 9299          # remote-debugging port for our Chrome instance
_NEW_CHAT   = "https://aistudio.google.com/prompts/new_chat"
_AI_HOST    = "aistudio.google.com"

_PROMPT = (
    "Tewende berilen tekstni Uyghur tiligha tercime qil. "
    "Barliq markdown formatlishini (# ## *, kod blokliri, jediwilar) saqlap qal. "
    "Paqat tercimini yaz, izahat qoshma.\n\n"
    "Tekst:\n{text}"
)

_LIMIT_WORDS = [
    "quota exceeded", "rate limit", "too many requests",
    "limit reached", "you've reached", "resource has been exhausted",
    "free quota", "upgrade your plan", "upgrade to",
]

_INPUT_SELS = [
    'ms-prompt-input-wrapper [contenteditable="true"]',
    'rich-textarea [contenteditable="true"]',
    '.ql-editor[contenteditable="true"]',
    '[contenteditable="true"][data-placeholder]',
    '[contenteditable="true"]',
    'textarea[aria-label]',
    'textarea',
]

_RUN_SELS = [
    'button[aria-label="Run"]',
    'button[aria-label="Send message"]',
    'button[aria-label="Submit"]',
    'run-button button',
    '[data-test-id="run-button"]',
    'button.send-button',
]

_RESP_SELS = [
    'ms-chat-turn model-response ms-cmark-node',
    'ms-chat-turn .markdown-main-panel',
    'ms-chat-turn ms-text-chunk',
    'ms-chat-turn .response-container',
    '.model-response-text',
]

_STOP_SEL = (
    'button[aria-label="Stop generating"], '
    'button[aria-label="Stop"], '
    'button[aria-label="Cancel"]'
)

# ── Chrome finder ─────────────────────────────────────────────────────────────

def _find_chrome() -> str:
    # Windows registry
    try:
        import winreg
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe",
        )
        path = winreg.QueryValue(key, None)
        if path and os.path.exists(path):
            return path
    except Exception:
        pass

    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
        r"C:\Program Files\Chromium\Application\chromium.exe",
    ]
    for p in candidates:
        if os.path.exists(p):
            return p

    raise FileNotFoundError(
        "Chrome tapilmidi!  Qolungiz bilen yolini kiriting (CHROME_PATH)."
    )


# ── translator ────────────────────────────────────────────────────────────────

class AIStudioTranslator:
    def __init__(self, accounts: list, profiles_dir: Path):
        self.accounts     = accounts
        self.profiles_dir = profiles_dir
        self._idx         = 0
        self._chrome      = None   # subprocess.Popen
        self._pw          = None
        self._browser     = None
        self._page        = None
        self._boot()

    # ── lifecycle ────────────────────────────────────────────────────────────

    def _boot(self):
        self._teardown()
        profile = self._profile_dir(self._idx)
        self._launch_chrome(profile)
        self._connect_cdp()
        self._open_ai_studio()

    def _teardown(self):
        try:
            if self._browser:
                self._browser.close()
        except Exception:
            pass
        try:
            if self._pw:
                self._pw.stop()
        except Exception:
            pass
        try:
            if self._chrome and self._chrome.poll() is None:
                self._chrome.terminate()
                self._chrome.wait(timeout=5)
        except Exception:
            pass
        self._chrome = self._pw = self._browser = self._page = None

    def close(self):
        self._teardown()

    # ── profile dir ──────────────────────────────────────────────────────────

    def _profile_dir(self, idx: int) -> str:
        slug = (
            self.accounts[idx]["email"]
            .replace("@", "_at_")
            .replace(".", "_")
        )
        p = self.profiles_dir / f"a{idx}_{slug}"
        p.mkdir(parents=True, exist_ok=True)
        return str(p)

    # ── Chrome launch ────────────────────────────────────────────────────────

    def _launch_chrome(self, profile_dir: str):
        chrome = os.environ.get("CHROME_PATH") or _find_chrome()
        cmd = [
            chrome,
            f"--remote-debugging-port={_CDP_PORT}",
            f"--user-data-dir={profile_dir}",
            "--no-first-run",
            "--no-default-browser-check",
            "--start-maximized",
        ]
        print(f"  [CHROME] Achilwatidu...")
        self._chrome = subprocess.Popen(cmd)
        # Wait until Chrome's debugging endpoint is ready
        self._wait_cdp_ready()

    def _wait_cdp_ready(self, retries: int = 20):
        import urllib.request
        for _ in range(retries):
            try:
                urllib.request.urlopen(
                    f"http://localhost:{_CDP_PORT}/json/version", timeout=2
                )
                return
            except Exception:
                time.sleep(0.5)
        raise RuntimeError(
            f"Chrome CDP portiga ({_CDP_PORT}) ulanghili bolmidi."
        )

    # ── CDP connect ──────────────────────────────────────────────────────────

    def _connect_cdp(self):
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.connect_over_cdp(
            f"http://localhost:{_CDP_PORT}"
        )
        ctx   = self._browser.contexts[0] if self._browser.contexts else None
        pages = ctx.pages if ctx else []
        self._page = pages[0] if pages else (ctx or self._browser).new_page()

    # ── AI Studio ────────────────────────────────────────────────────────────

    def _open_ai_studio(self):
        try:
            self._page.goto(_NEW_CHAT, timeout=30_000, wait_until="domcontentloaded")
            self._page.wait_for_timeout(3000)
        except Exception as e:
            print(f"  [WARN] {e}")

        if _AI_HOST not in self._page.url:
            self._ask_manual_login()

        self._dismiss_dialogs()

    def _ask_manual_login(self):
        email = self.accounts[self._idx]["email"]
        print()
        print("  ╔══════════════════════════════════════════════════════════╗")
        print("  ║  Chrome achildi — qolungiz bilen kiriwalung             ║")
        print(f"  ║  Hisab: {email:<50} ║")
        print("  ║  AI Studio ge kirip bolsangiz bu yerde ENTER bassung.  ║")
        print("  ╚══════════════════════════════════════════════════════════╝")
        input("  >>> ENTER: ")
        try:
            self._page.goto(_NEW_CHAT, timeout=30_000, wait_until="domcontentloaded")
            self._page.wait_for_timeout(2000)
        except Exception:
            pass

    def _dismiss_dialogs(self):
        for sel in [
            'button:has-text("Got it")',
            'button:has-text("Accept")',
            'button:has-text("Agree")',
            'button:has-text("Continue")',
            'button:has-text("I agree")',
            'button[aria-label="Close"]',
        ]:
            try:
                btn = self._page.query_selector(sel)
                if btn and btn.is_visible():
                    btn.click()
                    self._page.wait_for_timeout(600)
            except Exception:
                pass

    # ── account rotation ─────────────────────────────────────────────────────

    def _rotate(self) -> bool:
        nxt = self._idx + 1
        if nxt >= len(self.accounts):
            print("[ERROR] Hemme hisablarning kunlik cheki toldi!")
            return False
        self._idx = nxt
        print(f"  [SWITCH] {nxt + 1}-hisabqa otiwatidu: {self.accounts[nxt]['email']}")
        self._boot()
        return True

    def _limit_reached(self) -> bool:
        try:
            low = self._page.content().lower()
            return any(w in low for w in _LIMIT_WORDS)
        except Exception:
            return False

    # ── helpers ──────────────────────────────────────────────────────────────

    def _find_first(self, sels: list, timeout: int = 8000):
        for sel in sels:
            try:
                el = self._page.wait_for_selector(sel, timeout=timeout, state="visible")
                if el:
                    return el
            except Exception:
                continue
        return None

    def _click_first(self, sels: list) -> bool:
        for sel in sels:
            try:
                el = self._page.query_selector(sel)
                if el and el.is_visible() and el.is_enabled():
                    el.click()
                    return True
            except Exception:
                continue
        return False

    def _set_text(self, inp, text: str):
        """Inject text via JS; keyboard fallback."""
        try:
            inp.evaluate(
                """(el, txt) => {
                    el.focus();
                    el.innerText = txt;
                    el.dispatchEvent(new Event('input',  { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                }""",
                text,
            )
            self._page.wait_for_timeout(400)
            val = inp.evaluate("el => el.innerText || el.value || ''")
            if val and len(val.strip()) > 10:
                return
        except Exception:
            pass
        # Keyboard fallback
        inp.click()
        self._page.wait_for_timeout(200)
        self._page.keyboard.press("Control+a")
        self._page.wait_for_timeout(150)
        self._page.keyboard.type(text, delay=5)

    def _wait_done(self):
        try:
            self._page.wait_for_selector(_STOP_SEL, timeout=10_000, state="visible")
            self._page.wait_for_selector(_STOP_SEL, timeout=180_000, state="hidden")
        except PWTimeout:
            print("  [WARN] Jawab tugishi kutilmidi, devam etildi.")
            self._page.wait_for_timeout(5000)
        except Exception:
            self._page.wait_for_timeout(6000)

    def _extract(self) -> str:
        for sel in _RESP_SELS:
            try:
                els = self._page.query_selector_all(sel)
                if els:
                    txt = els[-1].inner_text().strip()
                    if txt:
                        return txt
            except Exception:
                continue
        try:
            turns = self._page.query_selector_all("ms-chat-turn")
            if turns:
                return turns[-1].inner_text().strip()
        except Exception:
            pass
        return ""

    # ── public API ───────────────────────────────────────────────────────────

    def translate(self, text: str, retries: int = 3) -> str:
        prompt = _PROMPT.format(text=text)
        for attempt in range(retries):
            try:
                result = self._do_translate(prompt)
                if result:
                    return result
                if self._limit_reached():
                    if not self._rotate():
                        return ""
            except Exception as e:
                print(f"  [WARN] Urinish {attempt + 1}/{retries}: {e}")
                if attempt < retries - 1:
                    time.sleep(3)
        return ""

    def _do_translate(self, prompt: str) -> str:
        self._page.goto(_NEW_CHAT, timeout=30_000, wait_until="domcontentloaded")
        self._page.wait_for_timeout(2000)

        # If session expired, ask user to re-login
        if _AI_HOST not in self._page.url:
            self._ask_manual_login()

        self._dismiss_dialogs()

        inp = self._find_first(_INPUT_SELS)
        if not inp:
            raise RuntimeError("AI Studio kirish maydani tapilmidi!")

        self._set_text(inp, prompt)
        self._page.wait_for_timeout(500)

        if not self._click_first(_RUN_SELS):
            inp.press("Control+Enter")

        self._wait_done()
        self._page.wait_for_timeout(700)

        return self._extract()
