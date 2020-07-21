# Created by gabrielavilaro at 20/07/2020
@selenium
Feature: Test page automationpractice.com

  @Browser
  Scenario: Open Browser
    Given Open Browser Aplication

  @Browser
  Scenario: Open url
    Given I start the app in the URL http://automationpractice.com/index.php
    Then I click on sign in
    And I write the email in the email address field
    And I click on create an account
    And I assert that the title of the create an account page is AUTHENTICATION
