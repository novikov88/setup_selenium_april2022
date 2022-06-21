from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure
from selenium.common.exceptions import TimeoutException


class CatalogPage(BasePage):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-primary1")
    PRODUCT_COMPARE_TEXT = (By.PARTIAL_LINK_TEXT, "Product Compare (0)1")
    CARD_PRODUCT = (By.CSS_SELECTOR, ".product-thumb1")

    def product_compare_check(self):
        self._click(self.PRODUCT_COMPARE_TEXT)

    def back_to_main_page(self):
        self._click(self.CONTINUE_BUTTON)

    def calculate_product_card(self):
        with allure.step(f"Ищу все элементы {self.CARD_PRODUCT}"):
            try:
                self.logger.info(f"Search all items {self.CARD_PRODUCT}")
                count_items = self.browser.find_elements(*self.CARD_PRODUCT)
                return count_items
            except TimeoutException:
                self.add_screenshot_to_allure(self.CARD_PRODUCT)
                raise AssertionError(f"Couldn't find items: {self.CARD_PRODUCT} on page {self.browser.current_url}")
