from uuid import uuid4

import pytest
from playwright.sync_api import Page, expect, sync_playwright
from searchproduct_page import SearchproductPage
from addtocart_page import Addtopage
from Signup.login_page import SignupPage
from shipping_order_payment import Shippingpage


def _signup_credentials() -> dict[str, str]:
    return {
        "username": "December",
        "email": f"december_{uuid4().hex[:10]}@example.com",
        "password": "december!",
        "birth_day": "9",
        "birth_month": "5",
        "birth_year": "2002",
        "first_name": "December",
        "last_name": "Month",
        "company": "Automation QA",
        "address": "32 Westlands Street",
        "address_2": "22 Eastlands Street",
        "country": "Australia",
        "state": "Denmark",
        "city": "Sydney",
        "zipcode": "00022",
        "mobile_number": "87654321235",
    }


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        try:
            yield page
        finally:
            browser.close()
        


def test_homepage_loads(page: Page):
    page.goto("https://automationexercise.com/")

    expect(page).to_have_title("Automation Exercise")


def test_search_product(page: Page):
    SearchproductPage(page).search_product("Top")
    page.pause()

def test_add_to_cart(page: Page):
    product_name = "Blue Top"
    Addtopage(page).add_to_cart(product_name)

def test_signup(page: Page):
    SignupPage(page).register(**_signup_credentials())
    page.get_by_role("link", name="Delete Account").click()
    expect(page.locator("data-test=\"delete-account\"]")).to_be_visible()

def test_login(page: Page):
    page.goto("https://automationexercise.com/login")
    login = SignupPage(page)
    login.enter_login_email("december@gmail.com")
    login.enter_password("december")
    login.click_login_button()

def test_proceed_to_checkout(page: Page):
    credentials = _signup_credentials()
    SignupPage(page).register(**credentials)
    page.get_by_text("Continue", exact=True).click()
    expect(page.get_by_text(f"Logged in as {credentials['username']}")).to_be_visible()
    Addtopage(page).add_to_cart("Blue Top")
    Shippingpage(page).proceed_to_payment()

def test_enter_payment_details(page: Page):
    shipping_page = Shippingpage(page)

    shipping_page.enter_payment_details()
