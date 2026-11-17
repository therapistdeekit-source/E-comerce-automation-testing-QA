import re

from playwright.sync_api import Page, expect
from pytest_bdd import given, scenario, then, when

from addtocart_page import Addtopage
from searchproduct_page import SearchproductPage


@scenario("../features/storefront.feature", "Homepage loads")
def test_homepage_loads():
    pass


@scenario("../features/storefront.feature", "Search for products")
def test_search_for_products():
    pass


@scenario("../features/storefront.feature", "Add a product to the cart")
def test_add_a_product_to_the_cart():
    pass


@given("I open the storefront")
def open_storefront(page: Page) -> None:
    page.goto("https://automationexercise.com/", wait_until="domcontentloaded")


@then("the homepage is displayed")
def homepage_is_displayed(page: Page) -> None:
    expect(page).to_have_title("Automation Exercise")


@given("I am on the product listing")
def open_product_listing(page: Page) -> None:
    page.goto("https://automationexercise.com/products", wait_until="domcontentloaded")


@when('I search for "Top"')
def search_for_top(page: Page) -> None:
    SearchproductPage(page).search_product("Top")


@then("matching products are displayed")
def matching_products_are_displayed(page: Page) -> None:
    expect(page.get_by_role("heading", name="Searched Products")).to_be_visible()
    expect(page.locator(".productinfo.text-center").first).to_be_visible()


@when('I add "Blue Top" to the cart')
def add_blue_top_to_cart(page: Page) -> None:
    Addtopage(page).add_to_cart("Blue Top")


@then('"Blue Top" is visible in the cart')
def blue_top_is_visible_in_cart(page: Page) -> None:
    expect(page).to_have_url(re.compile(r".*/view_cart$"))
    expect(page.locator("tbody tr").filter(has_text="Blue Top")).to_be_visible()
