

import pytest
from playwright.sync_api import Page, expect


class Shippingpage:
    def __init__(self, page: Page):
        self.page = page

    def proceed_to_checkout(self) -> None:
        self.page.goto("https://automationexercise.com/view_cart")
        self.page.get_by_text("Proceed To Checkout").click()
        expect(self.page.get_by_role("link", name="Place Order")).to_be_visible()
        self.page.get_by_role("link", name="Place Order").click()
        self.page.locator("iframe[name=\"aswift_2\"]").content_frame.get_by_role("button", name="Close ad").click()
        expect(self.page.get_by_text("Home Payment Payment Name on")).to_be_visible()
        self.page.pause()

    @pytest.mark.regression
    def enter_payment_details(self) -> None:
        self.page.get_by_role("textbox", name="Name on Card").fill("December Month")
        self.page.get_by_role("textbox", name="Card Number").fill("1234 5678 9012 3456")
        self.page.get_by_role("textbox", name="CVC").fill("123")
        self.page.get_by_role("textbox", name="Expiration Month").fill("12")
        self.page.get_by_role("textbox", name="Expiration Year").fill("2025")

