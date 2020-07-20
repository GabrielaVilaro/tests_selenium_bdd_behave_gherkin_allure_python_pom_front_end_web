from behave import *
from functions.Functions import Functions as Selenium
use_step_matcher("re")


class StepsDefinitions():

    @given("Open Browser Aplication")
    def open_browser(self):
        Selenium.open_browser(self)

    @given("I start the app in the URL (.*)")
    def step_impl(self, URL):
        Selenium.open_browser(self, URL=URL)
