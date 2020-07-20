from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium import webdriver
from functions.Inicializar import Inicializar


class Functions(Inicializar):

    def open_browser(self, URL=Inicializar.URL, navegador=Inicializar.BROWSER):
            print(navegador)
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
        print("Se cerrará  el DRIVER")
        self.driver.quit()


