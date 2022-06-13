import allure
from page_objects.BasePage import BasePage
from faker import Faker
from selenium.webdriver.common.by import By

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

    @allure.step(f"Ищу все элементы radio buttons{RADIO_BUTTON}")
    def click_radio_buttons(self):
        self.logger.info(f"Find all elements {self.RADIO_BUTTON}")
        count_radio = self.browser.find_elements(*self.RADIO_BUTTON)
        for value in range(len(count_radio)):
            self._click(count_radio[value])

    @allure.step(f"Ищу все не активированные элементы check boxes{CHECK_BOX}")
    def activation_check_boxes(self):
        self.logger.info(f"Find all elements {self.CHECK_BOX}")
        count_check_boxes = self.browser.find_elements(*self.CHECK_BOX)
        for value in range(len(count_check_boxes)):
            self._click(count_check_boxes[value])

    @allure.step(f"Ищу все элементы активированные check boxes{CHECK_BOX}")
    def deactivation_check_boxes(self):
        self.logger.info(f"Find all elements {self.CHECK_BOX}")
        count_check_boxes = self.browser.find_elements(*self.CHECK_BOX)
        for value in range(len(count_check_boxes)):
            self._click(count_check_boxes[value])

    def set_text_in_field_text(self):
        self.input(self.TEXT_FIELD, fake.text())

    def set_text_in_field_text_area(self):
        self.input(self.TEXT_AREA_FIELD, fake.text())

    @allure.step(f"Ищу все элементы календаря {DAY_BUTTON}")
    def select_day_in_date_calendar(self):
        self._click(self.DATE_CALENDAR_BUTTON)
        self.logger.info(f"Choice in calendar value: {self.DAY_BUTTON}")
        self.browser.find_elements(*self.DAY_BUTTON)[0].click()
