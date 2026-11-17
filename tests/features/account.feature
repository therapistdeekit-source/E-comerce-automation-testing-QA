Feature: Customer accounts
  As a customer
  I want to register and log in
  So that I can use my account

  Scenario: Register a new account
    Given I have valid registration details
    When I create a customer account
    Then the account creation confirmation is displayed

  Scenario: Log in to an existing account
    Given I have a registered customer account
    When I log in with that account
    Then I am shown as logged in
