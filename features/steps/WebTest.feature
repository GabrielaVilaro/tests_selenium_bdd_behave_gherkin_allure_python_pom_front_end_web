# Created by gabrielavilaro at 20/07/2020
@selenium
Feature: Test page automationpractice.com

  @Browser
  Scenario: Open Browser
    Given Open Browser Aplication
    Then Close the browser

  @Browser
  Scenario: Open url, and assert page create an account
    Given I start the app in the URL http://automationpractice.com/index.php
    And I click on sign in
    And I write the email in the email address field
    When I click on create an account
    Then I assert that the title of the create an account page is AUTHENTICATION
    Then Close the browser

    @Browser
    Scenario: Open browser, assert phone number
      Given I start the app in the URL http://automationpractice.com/index.php
      And I assert number phone 0123-456-789
      Then Close the browser
