from behave import *
from functions.Functions import Functions as Selenium
from pages.page_create_account import PageCreateAnAccount
from pages.page_index import PageIndex
from pages.page_sign_in import PageSignIn
use_step_matcher("re")


class StepsDefinitions():

    @given("Open Browser Aplication")
    def open_browser(self):
        Selenium.open_browser(self)

    @given("I start the app in the URL (.*)")
    def step_impl(self, URL):
        Selenium.open_browser(self, URL=URL)

    @then("Close the browser")
    def step_impl(self):
        Selenium.tearDown(self)

    @step("I click on sign in")
    def step_impl(self):
        PageIndex.push_sign_in(self)

    @step("I write the email in the email address field")
    def step_impl(self):
        self.email = Selenium.generate_email(self)
        PageSignIn.send_email_create_an_acccount(self, self.email)

    @step('I click on create an account')
    def step_impl(self):
        PageSignIn.push_create_an_account_button(self)

    @step('I assert number phone (.*)')
    def step_impl(self, number_phone='0123-456-789'):
        self.phone_number_of_index_page = PageIndex.return_phone_number_of_banner(self)
        print('The number phone is: ' + self.phone_number_of_index_page)
        assert self.phone_number_of_index_page == number_phone, 'Not macht'

    @step('I assert that the title of the create an account page is (.*)')
    def step_impl(self, title='AUTHENTICATION'):
        self.title_on_page_create_an_Account = PageCreateAnAccount.return_title_of_create_authentication(self)
        print('Titile of page: ' + self.title_on_page_create_an_Account)
        assert self.title_on_page_create_an_Account == title, 'Not match'



