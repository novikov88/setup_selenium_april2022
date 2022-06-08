from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.browser.save_screenshot(f"{self.browser.session_id}.png")
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).move_to_element(element).click().perform()

    def _verify_elements_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.browser.save_screenshot(f"{self.browser.session_id}.png")
            raise AssertionError("Cant find elements by locator: {}".format(locator))

    def _elements(self, locator: tuple):
        return self._verify_elements_presence(locator)
