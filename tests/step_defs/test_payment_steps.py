from pytest_bdd import given, scenario, then, when
from playwright.sync_api import Page, expect

from shipping_order_payment import PaymentPage


@scenario(
    "../features/payment.feature",
    "Complete payment with valid test card details",
)
def test_complete_payment():
    pass


@given("I am on the payment page")
def open_payment_page(page: Page) -> None:
    page.goto("https://automationexercise.com/payment", wait_until="domcontentloaded")


@when("I submit valid test card details")
def submit_test_card_details(page: Page) -> None:
    PaymentPage(page).complete_payment(
        name_on_card="Test Customer",
        card_number="4111111111111111",
        cvc="123",
        expiry_month="12",
        expiry_year="2030",
    )


@then("the order confirmation is displayed")
def verify_order_confirmation(page: Page) -> None:
    expect(page.get_by_text("ORDER PLACED!")).to_be_visible()
