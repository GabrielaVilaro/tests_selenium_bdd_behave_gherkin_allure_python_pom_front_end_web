from behave import *
from functions.Functions import Functions as Selenium
from pages.page_create_account import PageCreateAnAccount
from pages.page_index import PageIndex
from pages.page_sign_in import PageSignIn
from user.user_static import StaticUserRegistered
from pages.page_my_account import PageMyAccount

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
    def step_impl(self, number_phone=r'[^0-9]'):
        self.phone_number_of_index_page = PageIndex.return_phone_number_of_banner(self)
        print('The number phone is: ' + self.phone_number_of_index_page)
        assert self.phone_number_of_index_page == number_phone, 'Not macht'

    @step('I assert that the title of the create an account page is (.*)')
    def step_impl(self, title='AUTHENTICATION'):
        title_on_page_create_an_Account = PageCreateAnAccount.return_title_of_create_authentication(self)
        print('Title of page: ' + title_on_page_create_an_Account)
        assert title_on_page_create_an_Account == title, 'Not match'

    @step('I login with user static registered')
    def step_impl(self):
        self.static_user = StaticUserRegistered()
        user_email = self.static_user.email_user_registered
        user_password = self.static_user.password_user_registered
        PageSignIn.send_email_user_registered(self, user_email)
        PageSignIn.send_password_user_registered(self, user_password)
        PageSignIn.push_sig_in_button(self)
        print('User e-mail registered is: ' + user_email)


    @step('I assert the name of account user is Test User')
    def step_impl(self):
        name_of_user_registered = PageMyAccount.return_text_user_registered(self)
        print(name_of_user_registered)
        assert name_of_user_registered == 'Test User', 'Not match'
