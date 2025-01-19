# Created by roynouneh at 2025-01-19
Feature: Adding Target products to cart
  # Enter feature description here

  Scenario: Make sure add to cart button works for the first product when searching for a Lenovo Legion Go
    Given We are on the Target home page
    When Search for a Lenovo Legion Go
    When Click on the search icon
    When Click on add to cart for the result in position 0
    When Click on add to cart from the sidebar
    When Exit the sidebar
    When Open the cart
    Then Expect product to be added