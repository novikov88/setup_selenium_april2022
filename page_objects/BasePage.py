from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure


class BasePage:
    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.handlers[:] = [file_handler]
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step("Кликаю в элемент {locator}")
    def _click(self, locator: tuple):
        try:
            self.logger.info("Click on element: {}".format(locator))
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            self.browser.save_screenshot(f"{self.browser.session_id}.png")
            raise AssertionError("CFailed to click on element: {}".format(locator))

    @allure.step("Ищу элемент {locator}")
    def _element(self, locator: tuple):
        try:
            self.logger.info("Check if element {} is present".format(locator))
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.browser.save_screenshot(f"{self.browser.session_id}.png")
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Ищу все элементы {locator}")
    def _elements(self, locator: tuple):
        try:
            self.logger.info("Check if elements {} is present".format(locator))
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.browser.save_screenshot(f"{self.browser.session_id}.png")
            raise AssertionError("Cant find elements by locator: {}".format(locator))

    @allure.step("Ввожу '{value}' в элемент {locator}")
    def input(self, locator, value):
        try:
            self.logger.info("Input: {} in input: {}".format(value, locator))
            find_field = self.wait.until(EC.presence_of_element_located(locator))
            find_field.click()
            find_field.clear()
            find_field.send_keys(value)
        except TimeoutException:
            self.browser.save_screenshot(f"{self.browser.session_id}.png")
            raise AssertionError("Failed to complete the field: {}".format(locator))
