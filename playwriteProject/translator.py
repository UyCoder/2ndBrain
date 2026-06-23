"""
Google AI Studio browser automation — Uyghur translation.
Smart login: watches the page state in a loop, auto-fills
email/password when visible, and waits for the user to complete
any extra Google verification (PIN, phone, 2FA, captcha, etc.).
"""

import time
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

_NEW_CHAT = "https://aistudio.google.com/prompts/new_chat"

_PROMPT = (
    "Tewende berilen tekstni Uyghur tiligha tercime qil. "
    "Barliq markdown formatlishini (# ## *, kod blokliri, jediwilar va bashqilar) saqlap qal. "
    "Paqat tercimini yaz, izahat yaki qoshimche nerse qoshma.\n\n"
    "Tekst:\n"
    "{text}"
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


class AIStudioTranslator:
    def __init__(self, accounts: list, profiles_dir: Path):
        self.accounts = accounts
        self.profiles_dir = profiles_dir
        self._idx = 0
        self._pw = None
        self._ctx = None
        self._page = None
        self._boot()

    # ── lifecycle ────────────────────────────────────────────────────────────

    def _boot(self):
        self._teardown()
        self._pw = sync_playwright().start()
        pdir = self._profile_dir(self._idx)
        self._ctx = self._pw.chromium.launch_persistent_context(
            user_data_dir=pdir,
            headless=False,
            slow_mo=30,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars",
            ],
            no_viewport=True,
        )
        pages = self._ctx.pages
        self._page = pages[0] if pages else self._ctx.new_page()
        self._go_and_login()

    def _teardown(self):
        for obj, method in [(self._ctx, "close"), (self._pw, "stop")]:
            if obj:
                try:
                    getattr(obj, method)()
                except Exception:
                    pass
        self._pw = self._ctx = self._page = None

    def close(self):
        self._teardown()

    # ── profile ──────────────────────────────────────────────────────────────

    def _profile_dir(self, idx: int) -> str:
        slug = (
            self.accounts[idx]["email"]
            .replace("@", "_at_")
            .replace(".", "_")
        )
        p = self.profiles_dir / f"a{idx}_{slug}"
        p.mkdir(parents=True, exist_ok=True)
        return str(p)

    # ── smart login ──────────────────────────────────────────────────────────

    def _go_and_login(self):
        """Navigate to AI Studio; if login is needed, handle it smartly."""
        try:
            self._page.goto(_NEW_CHAT, timeout=30_000, wait_until="domcontentloaded")
            self._page.wait_for_timeout(2000)
        except Exception as e:
            print(f"  [WARN] Sahipe ochmidi: {e}")

        if "aistudio.google.com" in self._page.url:
            self._dismiss_dialogs()
            return  # already logged in (saved profile)

        # Need to login
        self._smart_login()
        self._dismiss_dialogs()

    def _smart_login(self):
        """
        Watch the browser page in a loop.
        - Auto-fills email when the email field appears.
        - Auto-fills password when the password field appears.
        - Clicks the correct account in the account-chooser if visible.
        - For ANY other step (PIN, phone, 2FA, captcha …) prints a
          one-time notice and keeps waiting until the user passes it.
        - Stops as soon as aistudio.google.com is reached.
        """
        email = self.accounts[self._idx]["email"]
        pwd   = self.accounts[self._idx]["password"]

        print(f"  [LOGIN] {email} bilen kiriwatidu...")

        filled_email    = False
        filled_password = False
        extra_notified  = False   # shown the "extra step" message?
        deadline        = time.time() + 300  # 5-minute overall timeout

        while time.time() < deadline:
            # ── success ──────────────────────────────────────────────────
            if "aistudio.google.com" in self._page.url:
                print("  [LOGIN] Kirish mewepiyetlik!")
                return

            # ── account chooser ──────────────────────────────────────────
            # Google shows a list of previously signed-in accounts
            try:
                acct_el = self._page.query_selector(
                    f'[data-identifier="{email}"], '
                    f'[data-email="{email}"], '
                    f'li[aria-label*="{email}"]'
                )
                if acct_el and acct_el.is_visible():
                    acct_el.click()
                    filled_email = True
                    extra_notified = False
                    self._page.wait_for_timeout(2000)
                    continue
            except Exception:
                pass

            # ── "Use another account" ────────────────────────────────────
            if not filled_email:
                try:
                    for sel in [
                        'li:has-text("Use another account")',
                        'div[role="link"]:has-text("Use another account")',
                        '[data-action="add"]',
                    ]:
                        el = self._page.query_selector(sel)
                        if el and el.is_visible():
                            el.click()
                            self._page.wait_for_timeout(2000)
                            break
                except Exception:
                    pass

            # ── email field ──────────────────────────────────────────────
            if not filled_email:
                try:
                    for sel in [
                        'input[type="email"]',
                        'input[name="identifier"]',
                        'input[autocomplete="username"]',
                        '#identifierId',
                    ]:
                        el = self._page.query_selector(sel)
                        if el and el.is_visible():
                            el.fill(email)
                            self._page.wait_for_timeout(500)
                            self._page.keyboard.press("Enter")
                            filled_email = True
                            extra_notified = False
                            self._page.wait_for_timeout(2000)
                            break
                except Exception:
                    pass
                if filled_email:
                    continue

            # ── password field ───────────────────────────────────────────
            if filled_email and not filled_password:
                try:
                    for sel in [
                        'input[type="password"]',
                        'input[name="password"]',
                        'input[autocomplete="current-password"]',
                    ]:
                        el = self._page.query_selector(sel)
                        if el and el.is_visible():
                            el.fill(pwd)
                            self._page.wait_for_timeout(500)
                            self._page.keyboard.press("Enter")
                            filled_password = True
                            extra_notified = False
                            self._page.wait_for_timeout(2000)
                            break
                except Exception:
                    pass
                if filled_password:
                    continue

            # ── unknown / extra step ─────────────────────────────────────
            # (PIN, 2FA, phone verification, "I'm not a robot", etc.)
            if not extra_notified:
                print()
                print("  ╔══════════════════════════════════════════════════════╗")
                print("  ║  QOSHIMCHE QEDEM — BROWSERDA OZ QOLUNGIZ BILEN UTING ║")
                print("  ║  (PIN, telefon, 2FA, CAPTCHA, vs.)                   ║")
                print("  ║  Uting, program oz-ozi devam etidu.                  ║")
                print("  ╚══════════════════════════════════════════════════════╝")
                extra_notified = True

            self._page.wait_for_timeout(2000)

        # timed out — ask user to finish manually
        print()
        print("  [WARN] 5 minut ichide AI Studio ge kiriwalalmidi.")
        print("  Browser de oz qolungiz bilen kiriwalung, tamam bolsa ENTER bassung.")
        input("  >>> ENTER: ")
        try:
            self._page.goto(_NEW_CHAT, timeout=30_000, wait_until="domcontentloaded")
            self._page.wait_for_timeout(2000)
        except Exception:
            pass

    # ── dialogs ──────────────────────────────────────────────────────────────

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
                    self._page.wait_for_timeout(700)
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

    # ── element helpers ──────────────────────────────────────────────────────

    def _find_first(self, sels: list, timeout: int = 5000):
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
        """Inject text via JS; keyboard fallback if JS does not stick."""
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
            self._page.wait_for_timeout(500)
            val = inp.evaluate("el => el.innerText || el.value || ''")
            if val and len(val.strip()) > 10:
                return
        except Exception:
            pass

        inp.click()
        self._page.wait_for_timeout(300)
        self._page.keyboard.press("Control+a")
        self._page.wait_for_timeout(200)
        self._page.keyboard.type(text, delay=8)

    def _wait_done(self):
        try:
            self._page.wait_for_selector(_STOP_SEL, timeout=10_000, state="visible")
            self._page.wait_for_selector(_STOP_SEL, timeout=180_000, state="hidden")
        except PWTimeout:
            print("  [WARN] Jawab tugishi kutilmidi.")
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
                    time.sleep(4)
        return ""

    def _do_translate(self, prompt: str) -> str:
        self._page.goto(_NEW_CHAT, timeout=30_000, wait_until="domcontentloaded")
        self._page.wait_for_timeout(2500)

        # If redirected to login page, run smart login again
        if "aistudio.google.com" not in self._page.url:
            self._smart_login()
            self._dismiss_dialogs()

        inp = self._find_first(_INPUT_SELS, timeout=10_000)
        if not inp:
            raise RuntimeError("Kirish maydani (input) tapilmidi!")

        self._set_text(inp, prompt)
        self._page.wait_for_timeout(600)

        if not self._click_first(_RUN_SELS):
            inp.press("Control+Enter")

        self._wait_done()
        self._page.wait_for_timeout(800)

        return self._extract()
