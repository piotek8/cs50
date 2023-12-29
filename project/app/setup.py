from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from app.configuration import BasePage

from constants import COMPANY_POSITION_KEYWORDS_WORDS_SEARCH
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import asyncio


class Setup(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.search_field = (By.CSS_SELECTOR, "div[data-test='dropdown-element-kw'] input[type='text']")
        self.junior_position_field = (By.XPATH, "(//span[@class='core_cwn1p5a'])[30]")
        self.publication_time_24h = (By.XPATH, "(//span[@class='core_cwn1p5a'])[49]")
        self.show_offer_button = (By.CSS_SELECTOR, "div[class='core_s1cjjpc4'] button[class='size-large variant-primary core_b1fqykql']")

        self.announcements = (By.XPATH, "//div[@class='tiles_bcblkf7']")
        self.find_location = (By.CLASS_NAME, "tiles_lov4ye4")

        self.apply_quickly_button = (By.XPATH, "(//span[@class='s1u5ksyd'][normalize-space()='Aplikuj szybko'])[3]")
        self.apply_button = (By.XPATH, "(//a[@title='Aplikuj na ogłoszenie'])[3]")
        self.send_now_button = (By.CSS_SELECTOR, 'button[data-test="button-apply"]')
        self.submit_form_button = (By.XPATH, 'XPATH,// button[ @ type = "submit"]')

        self.send_form_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.skip_button = (By.CSS_SELECTOR, "button[type='button'] span[class='sm8uzh7']")

    def data_set(self):
        try:
            enter_data_into_search_field = self.driver.find_element(*self.search_field)
            enter_data_into_search_field.send_keys(COMPANY_POSITION_KEYWORDS_WORDS_SEARCH)

            enter_junior_position = self.wait.until(EC.element_to_be_clickable(self.junior_position_field))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", enter_junior_position)
            enter_junior_position.click()

            enter_publication = self.wait.until(EC.element_to_be_clickable(self.publication_time_24h))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", enter_publication)
            enter_publication.click()

            press_show_offer_button = self.driver.find_element(*self.show_offer_button)
            press_show_offer_button.click()


        except NoSuchElementException:
            print(
                f"The item could not be found. Check IDs: {self.search_field}, {self.junior_position_field}, {self.publication_time_24h}, {self.show_offer_button}")

        except Exception as e:
            print(f"An error occured: {e}")

    async def announcement_iteration(self):
        loop = asyncio.get_event_loop()
        try:
            self.driver.implicitly_wait(3)
            elements = self.driver.find_elements(*self.announcements)
            for element in elements:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                print(element)
                await loop.run_in_executor(None, ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                    Keys.CONTROL).perform)
                try:
                    WebDriverWait(self.driver, 0.5).until(EC.element_to_be_clickable(self.find_location)).click()
                except TimeoutException:
                    pass

                self.driver.switch_to.window(self.driver.window_handles[-1])

                try:
                    self.wait.until(EC.element_to_be_clickable(self.apply_button)).click()
                    self.wait.until(EC.element_to_be_clickable(self.send_now_button)).click()
                    self.wait.until(EC.element_to_be_clickable(self.skip_button)).click()
                    self.driver.close()
                except TimeoutException:
                    pass

                self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as e:
            print(e)



'''
    async def announcement_iteration(self):
        loop = asyncio.get_event_loop()
        try:
            self.driver.implicitly_wait(3)
            elements = self.driver.find_elements(*self.announcements)
            for element in elements:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                print(element)
                await loop.run_in_executor(None, ActionChains(self.driver).key_down(Keys.CONTROL).click(element).key_up(
                    Keys.CONTROL).perform)
                try:
                    WebDriverWait(self.driver, 0.5).until(EC.element_to_be_clickable(self.find_location)).click()
                except TimeoutException:
                    pass

                self.driver.switch_to.window(self.driver.window_handles[-1])

                try:
                    self.wait.until(EC.element_to_be_clickable(self.apply_button)).click()
                    self.wait.until(EC.element_to_be_clickable(self.send_now_button)).click()
                    self.wait.until(EC.element_to_be_clickable(self.skip_button)).click()
                    self.driver.close()
                except TimeoutException:
                    pass

                self.driver.switch_to.window(self.driver.window_handles[0])

        except Exception as e:
            print(e)
'''