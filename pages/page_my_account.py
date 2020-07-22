from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from functions.Functions import Functions


class PageMyAccount(Functions):

    def return_text_user_registered(self):
        self.name_of_user_registration = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span')
        text_user = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.name_of_user_registration))
        text = text_user.text
        return text

    def return_text_of_banner(self):
        self.title_of_banner = (By.XPATH, '//*[@id="center_column"]/h1')
        text_of_banner = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.title_of_banner))
        text = text_of_banner.text
        return text
