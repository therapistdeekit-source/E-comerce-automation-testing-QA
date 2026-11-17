Feature: Payment
  As a customer
  I want to submit payment details
  So that I can complete my order

  Scenario: Complete payment with valid test card details
    Given I am on the payment page
    When I submit valid test card details
    Then the order confirmation is displayed
