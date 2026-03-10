from pathlib import Path

from playwright.sync_api import sync_playwright


ROOT_DIR = Path(__file__).resolve().parent.parent
HTML_PATH = ROOT_DIR / "presentation" / "onboard-asof.html"
PDF_PATH = ROOT_DIR / "presentation" / "onboard-asof-web.pdf"


def render_pdf() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 990})
        page.goto(HTML_PATH.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(PDF_PATH),
            print_background=True,
            landscape=True,
            width="297mm",
            height="210mm",
            margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"},
            prefer_css_page_size=True,
        )
        browser.close()


if __name__ == "__main__":
    render_pdf()
