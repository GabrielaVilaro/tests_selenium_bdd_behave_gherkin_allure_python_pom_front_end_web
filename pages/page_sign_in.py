from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from functions.Functions import Functions


class PageSignIn(Functions):

    def send_email_create_an_acccount(self, text):
        self.box_email = (By.ID, 'email_create')
        send_email = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.box_email))
        send_email.send_keys(text)

    def push_create_an_account_button(self):
        self.button_created = (By.XPATH, '//*[@id="SubmitCreate"]/span')
        button_created = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_created))
        button_created.click()

    def push_sig_in_button(self):
        self.button_sign_in = (By.XPATH, '//*[@id="SubmitLogin"]/span')
        button_sign_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_sign_in))
        button_sign_in.click()

    def send_email_user_registered(self, text):
        self.box_password_registered = (By.ID, 'email')
        send_mail_registered = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.box_password_registered))
        send_mail_registered.send_keys(text)

    def send_password_user_registered(self, text):
        self.box_password_registered = (By.ID, 'passwd')
        send_mail_registered = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.box_password_registered))
        send_mail_registered.send_keys(text)







