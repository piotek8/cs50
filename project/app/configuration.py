from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from constants import LOGIN_PAGE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)


class ConfigurationManager:
    def get_driver_and_open_web(self):
        options = Options()
        options.add_experimental_option('detach', True)  # pozostaw otwartą przeglądarkę
        options.add_argument("--start-maximized")

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)
        driver.get(LOGIN_PAGE_URL)

        return driver
