from selenium.webdriver.common.by import By
from app.configuration import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        load_dotenv()

        self.username_field = (By.CSS_SELECTOR, "#email")
        self.password_field = (By.CSS_SELECTOR, "#password")
        self.next_and_login_button = (By.CSS_SELECTOR, "button[type='submit'] span[class='sm8uzh7']")

    def login_to_account(self):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        try:
            enter_username = self.wait.until(EC.visibility_of_element_located(self.username_field))
            enter_username.send_keys(email)

            next_button = self.wait.until(EC.element_to_be_clickable(self.next_and_login_button))
            next_button.click()

            enter_password = self.wait.until(EC.visibility_of_element_located(self.password_field))
            enter_password.send_keys(password)

            login_button = self.wait.until(EC.element_to_be_clickable(self.next_and_login_button))
            login_button.click()

        except NoSuchElementException:
            print(
                f"The item could not be found. Check IDs: {self.username_field}, {self.password_field}, {self.next_and_login_button}")
        except Exception as e:
            print(f"An error occured: {e}")

