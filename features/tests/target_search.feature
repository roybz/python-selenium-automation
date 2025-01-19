# Created by roynouneh at 2025-01-19
Feature: Target search steps
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Target home page
    When Populate search script with Table
    When Click on target search icon
    Then Product results for Table are displayed

  Scenario: User can search for a product
   Given Open Target home page
   When Populate search script with Tennis Shoes
   When Click on target search icon
   Then Product results for Tennis Shoes are displayed
