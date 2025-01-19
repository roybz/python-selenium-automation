# Created by roynouneh at 2025-01-19
Feature: Target Cart Features
  # Enter feature description here

  Scenario: Verify that the your cart is empty message is shown
    Given Open target.com
    When Click on cart icon
    Then Verify "Your cart is empty" message is shown