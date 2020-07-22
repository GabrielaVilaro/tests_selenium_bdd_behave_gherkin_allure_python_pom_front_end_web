from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium import webdriver
from functions.Inicializar import Inicializar
import random
import string


class Functions(Inicializar):

    def open_browser(self, URL=Inicializar.URL, browser=Inicializar.BROWSER):
        print(browser)
        options = OpcionesChrome()
        options.add_argument('start-maximized')
        self.driver = webdriver.Chrome(chrome_options=options,
                                       executable_path=Inicializar.basedir + "/driver/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.get(URL)
        self.driver.maximize_window()
        self.windows = {'Principal': self.driver.window_handles[0]}
        return self.driver

    def tearDown(self):
        print("Close the DRIVER")
        self.driver.quit()

     #Función que genera un email random
    def generate_email(self):
        self.prefix = 'test123+'
        self.domain = 'gmail.com'
        random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                        for _ in range(10))
        return self.prefix + random_part + '@' + self.domain

    def generate_number_phone(self):
        self.random_number = ''.join(random.choice(string.digits)
                                for _ in range(10))
        return self.random_number





