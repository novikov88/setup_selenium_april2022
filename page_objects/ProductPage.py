import allure
from page_objects.BasePage import BasePage
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# создаем экземпляр класса Faker для генерации данных
fake = Faker()


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='button-cart']")
    RADIO_BUTTON = (By.XPATH, "//input[@type='radio' and @name='option[218]']")
    CHECK_BOX = (By.XPATH, "//input[@type='checkbox' and @name='option[223][]']")
    TEXT_FIELD = (By.XPATH, "//input[@id='input-option208']")
    TEXT_AREA_FIELD = (By.CSS_SELECTOR, '#input-option209')
    DATE_CALENDAR_BUTTON = (By.CSS_SELECTOR, '.fa-calendar')
    DAY_BUTTON = (By.XPATH, "//td[@class='day active']")

    def add_to_cart_button_click(self):
        self._click(self.ADD_TO_CART_BUTTON)

    def click_radio_buttons(self):
        with allure.step(f"Ищу все элементы radio buttons{self.RADIO_BUTTON} и кликаю в найденные"):
            try:
                self.logger.info(f"Find all elements {self.RADIO_BUTTON}")
                count_radio = self.browser.find_elements(*self.RADIO_BUTTON)
                for value in range(len(count_radio)):
                    self._click(count_radio[value])
            except TimeoutException:
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="radio_button_screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Couldn't find items: {self.RADIO_BUTTON}")

    def activation_check_boxes(self):
        with allure.step(f"Ищу все не активированные элементы check boxes{self.CHECK_BOX} и кликаю в найденные"):
            try:
                self.logger.info(f"Find all elements {self.CHECK_BOX}")
                count_check_boxes = self.browser.find_elements(*self.CHECK_BOX)
                for value in range(len(count_check_boxes)):
                    self._click(count_check_boxes[value])
            except TimeoutException:
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="check_boxes_screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Couldn't find items: {self.CHECK_BOX}")

    def deactivation_check_boxes(self):
        with allure.step(f"Ищу все активированные элементы check boxes{self.CHECK_BOX} и кликаю в найденные"):
            try:
                self.logger.info(f"Find all elements {self.CHECK_BOX}")
                count_check_boxes = self.browser.find_elements(*self.CHECK_BOX)
                for value in range(len(count_check_boxes)):
                    self._click(count_check_boxes[value])
            except TimeoutException:
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="check_boxes_screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Couldn't find items: {self.CHECK_BOX}")

    def set_text_in_field_text(self):
        self.input(self.TEXT_FIELD, fake.text())

    def set_text_in_field_text_area(self):
        self.input(self.TEXT_AREA_FIELD, fake.text())

    def select_day_in_date_calendar(self):
        self._click(self.DATE_CALENDAR_BUTTON)
        self.logger.info(f"Choice in calendar value: {self.DAY_BUTTON}")
        with allure.step(f"Ищу все элементы в календаре и клик на нулевой {self.DAY_BUTTON}"):
            try:
                self.browser.find_elements(*self.DAY_BUTTON)[0].click()
            except TimeoutException:
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name="check_boxes_screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"Couldn't find items: {self.DAY_BUTTON}")
