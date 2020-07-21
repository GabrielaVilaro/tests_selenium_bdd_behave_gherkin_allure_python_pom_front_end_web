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
        self.button_create_an_account = (By.XPATH, '//*[@id="SubmitCreate"]/span')
        button_sign_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_create_an_account))
        button_sign_in.click()





