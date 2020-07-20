# Created by gabrielavilaro at 20/07/2020
@selenium
Feature: Funciones basicas de selenium con BDD

  @Navegador
  Scenario: Open Browser
    Given Open Browser Aplication

  @Navegador
  Scenario: Open url
    Given I start the app in the URL https://www.phptravels.net/home