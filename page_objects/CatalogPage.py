from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure


class CatalogPage(BasePage):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    PRODUCT_COMPARE_TEXT = (By.PARTIAL_LINK_TEXT, "Product Compare (0)")
    CARD_PRODUCT = (By.CSS_SELECTOR, ".product-thumb")

    def product_compare_check(self):
        self._click(self.PRODUCT_COMPARE_TEXT)

    def back_to_main_page(self):
        self._click(self.CONTINUE_BUTTON)

    @allure.step(f"Ищу все элементы {CARD_PRODUCT}")
    def calculate_product_card(self):
        self.logger.info(f"Search all items {self.CARD_PRODUCT}")
        count_items = self.browser.find_elements(*self.CARD_PRODUCT)
        return count_items
