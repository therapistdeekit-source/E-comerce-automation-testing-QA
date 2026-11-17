from uuid import uuid4

from playwright.sync_api import Page, expect
from pytest_bdd import given, scenario, then, when

from Signup.login_page import SignupPage


@scenario("../features/account.feature", "Register a new account")
def test_register_a_new_account():
    pass


@scenario("../features/account.feature", "Log in to an existing account")
def test_log_in_to_an_existing_account():
    pass


def _new_customer() -> dict[str, str]:
    return {
        "username": "BDD Customer",
        "email": f"bdd_{uuid4().hex[:12]}@example.com",
        "password": "bdd-test-password!",
        "birth_day": "9",
        "birth_month": "5",
        "birth_year": "2002",
        "first_name": "BDD",
        "last_name": "Customer",
        "company": "Automation QA",
        "address": "32 Westlands Street",
        "address_2": "22 Eastlands Street",
        "country": "Australia",
        "state": "Denmark",
        "city": "Sydney",
        "zipcode": "00022",
        "mobile_number": "87654321235",
    }


@given("I have valid registration details")
def valid_registration_details(customer: dict[str, str]) -> None:
    customer.update(_new_customer())


@when("I create a customer account")
def create_customer_account(page: Page, customer: dict[str, str]) -> None:
    SignupPage(page).register(**customer)


@then("the account creation confirmation is displayed")
def account_creation_confirmation_is_displayed(page: Page) -> None:
    expect(
        page.get_by_text(
            "Account Created! Congratulations! Your new account has been successfully"
        )
    ).to_be_visible()


@given("I have a registered customer account")
def registered_customer_account(
    page: Page, customer: dict[str, str]
) -> None:
    customer.update(_new_customer())
    SignupPage(page).register(**customer)
    page.get_by_text("Continue", exact=True).click()
    page.get_by_role("link", name="Logout").click()


@when("I log in with that account")
def log_in_with_account(page: Page, customer: dict[str, str]) -> None:
    page.goto("https://automationexercise.com/login", wait_until="domcontentloaded")
    login = SignupPage(page)
    login.enter_login_email(customer["email"])
    login.enter_password(customer["password"])
    login.click_login_button()


@then("I am shown as logged in")
def logged_in_as_customer(page: Page, customer: dict[str, str]) -> None:
    expect(page.get_by_text(f"Logged in as {customer['username']}")).to_be_visible()
