from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from functions.Functions import Functions


class PageIndex(Functions):

    def push_sign_in(self):
        self.button_sign_in = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        button_sign_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_sign_in))
        button_sign_in.click()

    def return_phone_number_of_banner(self):
        self.phone_numbre_of_banner = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/span/strong')
        phone_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.phone_numbre_of_banner))
        number = phone_number.text
        return number
