from selenium.webdriver.common.by import By
from faker import Faker
from page_objects.BasePage import BasePage

# создаем экземпляр класса Faker для генерации данных
fake = Faker()


class DashboardAdminPage(BasePage):
    NAVIGATION_PANEL = (By.CSS_SELECTOR, "#navigation")
    LOGOUT_BUTTON = (By.XPATH, "//span[contains(text(),'Logout')]")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCT_MENU = (By.XPATH, "//a[contains(text(),'Products')]")
    BUTTON_ADD = (By.XPATH, "//a[@data-original-title='Add New']")
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name1')
    DESCRIPTION_FIELD = (By.XPATH, "//div[@class='note-editable' and @role='textbox']")
    META_TAG_FIELD = (By.XPATH, "//input[@id = 'input-meta-title1']")
    GENERAL_TAB = (By.XPATH, "//a[contains(text(),'General')]")
    DATA_TAB = (By.XPATH, "//a[contains(text(),'Data')]")
    MODEL_FIELD = (By.CSS_SELECTOR, '#input-model')
    PRICE_FIELD = (By.XPATH, "//input[@id='input-price']")
    IMAGE_TAB = (By.XPATH, "//a[contains(text(),'Image')]")
    IMAGE_BUTTON = (By.CSS_SELECTOR, '#thumb-image')
    PENCIL_BUTTON = (By.XPATH, "//i[@class='fa fa-pencil']")
    IMAGE = (By.CSS_SELECTOR, ".col-xs-6")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit' and @form='form-product']")
    CHECK_BOX_PRODUCT = (By.XPATH, "//input[@type='checkbox' and @name='selected[]']")
    DELETE_BUTTON = (By.XPATH, "//button[@type='button' and @data-original-title='Delete']")
    NEW_PRODUCT = (By.XPATH, "//td[contains(text(),'Vertu-7')]")

    def navigation_panel_check(self):
        self._element(self.NAVIGATION_PANEL)

    def logout(self):
        self._click(self.LOGOUT_BUTTON)

    def go_to_section_adding_product(self):
        self._click(self.CATALOG_MENU)
        self._click(self.PRODUCT_MENU)
        self._click(self.BUTTON_ADD)

    def set_product_name(self):
        self._click(self.PRODUCT_NAME_FIELD)
        self.browser.find_element(*self.PRODUCT_NAME_FIELD).clear()
        self.browser.find_element(*self.PRODUCT_NAME_FIELD).send_keys('Vertu-7')

    def set_description(self):
        self._click(self.DESCRIPTION_FIELD)
        self.browser.find_element(*self.DESCRIPTION_FIELD).clear()
        self.browser.find_element(*self.DESCRIPTION_FIELD).send_keys(fake.text())

    def set_meta_tag(self):
        self._click(self.META_TAG_FIELD)
        self.browser.find_element(*self.META_TAG_FIELD).clear()
        self.browser.find_element(*self.META_TAG_FIELD).send_keys('Vertu')

    def go_to_data_tab(self):
        self._click(self.DATA_TAB)

    def set_model(self):
        self._click(self.MODEL_FIELD)
        self.browser.find_element(*self.MODEL_FIELD).clear()
        self.browser.find_element(*self.MODEL_FIELD).send_keys('7')

    def set_price(self):
        self._click(self.PRICE_FIELD)
        self.browser.find_element(*self.PRICE_FIELD).clear()
        self.browser.find_element(*self.PRICE_FIELD).send_keys('3200')

    def go_to_image_tab(self):
        self._click(self.IMAGE_TAB)

    def save_product(self):
        self._click(self.SAVE_BUTTON)

    def check_product(self):
        self._element(self.NEW_PRODUCT)

    def go_to_section_all_products(self):
        self._click(self.CATALOG_MENU)
        self._click(self.PRODUCT_MENU)

    def choose_a_product(self):
        self._elements(self.CHECK_BOX_PRODUCT)[-1].click()

    def delete_a_product(self):
        self._click(self.DELETE_BUTTON)
        alert = self.browser.switch_to.alert
        alert.accept()
