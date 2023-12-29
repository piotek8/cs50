from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from configuration import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.cookies = ".size-medium.variant-primary.core_b1fqykql"
        self.home_page = "div[class='header_l1ro2ilk'] img[alt='Logo Pracuj.pl']"
        self.IT_button = 'span[data-test="tab-item-it"]'
        self.search = ".size-large.variant-primary.core_b1fqykql"

    def navigate_home(self):
        try:
            accept_cookies = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.cookies)))
            accept_cookies.click() if accept_cookies else None

            go_to_homepage_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.home_page)))
            go_to_homepage_button.click()

            search_button = self.driver.find_element(By.CSS_SELECTOR, self.IT_button)
            search_button.click()

            search_button = self.driver.find_element(By.CSS_SELECTOR, self.search)
            search_button.click()

        except NoSuchElementException:
            print(f"The item could not be found. Check selectors: {self.cookies}, {self.home_page}, {self.search}")
        except Exception as e:
            print(f"An error occured: {e}")