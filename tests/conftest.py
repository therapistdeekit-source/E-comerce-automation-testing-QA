import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        try:
            yield page
        finally:
            browser.close()


@pytest.fixture
def customer() -> dict[str, str]:
    return {}
