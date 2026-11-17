

from playwright.sync_api import Page, expect


class PaymentPage:
    def __init__(self, page: Page):
        self.page = page

    def complete_payment(
        self,
        *,
        name_on_card: str,
        card_number: str,
        cvc: str,
        expiry_month: str,
        expiry_year: str,
    ) -> None:
        expect(self.page.get_by_role("heading", name="Payment")).to_be_visible()
        self.page.locator('[name="name_on_card"]').fill(name_on_card)
        self.page.locator('[name="card_number"]').fill(card_number)
        self.page.locator('[name="cvc"]').fill(cvc)
        self.page.locator('[name="expiry_month"]').fill(expiry_month)
        self.page.locator('[name="expiry_year"]').fill(expiry_year)
        self.page.get_by_role("button", name="Pay and Confirm Order").click()
        expect(self.page.get_by_text("ORDER PLACED!")).to_be_visible()
