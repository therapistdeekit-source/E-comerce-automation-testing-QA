from playwright.sync_api import expect


class Addtopage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, product_name: str) -> None:
        self.page.goto(
            "https://automationexercise.com/products",
            wait_until="domcontentloaded",
        )

        product = self.page.locator(".product-image-wrapper").filter(
            has=self.page.locator(".productinfo p").filter(has_text=product_name)
        )

        expect(product).to_have_count(1)
        product.locator("a.add-to-cart").first.click()

        expect(self.page.get_by_text("Added! Your product has")).to_be_visible()
        self.page.get_by_role("link", name="View Cart").click()

        cart_row = self.page.locator("tbody tr").filter(has_text=product_name)
        expect(cart_row).to_be_visible()
