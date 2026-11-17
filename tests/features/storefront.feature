Feature: Storefront
  As a shopper
  I want to browse and search products
  So that I can find items to purchase

  Scenario: Homepage loads
    Given I open the storefront
    Then the homepage is displayed

  Scenario: Search for products
    Given I am on the product listing
    When I search for "Top"
    Then matching products are displayed

  Scenario: Add a product to the cart
    When I add "Blue Top" to the cart
    Then "Blue Top" is visible in the cart
