# Created by roynouneh at 2025-01-19
Feature: Target Signin Features
  # Enter feature description here

  Scenario: Users can navigate to SignIn page
    Given Open Target main page
    When Click sign in button from header
    When Click on the signin button in the sidebar
    Then Verify sign in form opened