from playwright.sync_api import Page, expect


class SearchproductPage:
    def __init__(self, page: Page):
        self.page = page

    def search_product(self, product_name: str) -> None:
        self.page.goto("https://automationexercise.com/products")
        self.page.locator("#search_product").fill(product_name)
        self.page.locator("#submit_search").click()

        expect(self.page.get_by_role("heading", name="Searched Products")).to_be_visible()
        expect(self.page.locator(".productinfo.text-center").first).to_be_visible()
