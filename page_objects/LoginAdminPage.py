from selenium.webdriver.common.by import By
from faker import Faker
from page_objects.BasePage import BasePage

# создаем экземпляр класса Faker для генерации данных
fake = Faker()


class LoginAdminPage(BasePage):
    PANEL_TITLE = (By.CSS_SELECTOR, ".panel-title")
    USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    NAVIGATION_PANEL = (By.CSS_SELECTOR, "#navigation")

    def successful_authorization_by_admin(self):
        self._click(self.USERNAME_FIELD)
        self.browser.find_element(*self.USERNAME_FIELD).clear()
        self.browser.find_element(*self.USERNAME_FIELD).send_keys("user")
        self._click(self.PASSWORD_FIELD)
        self.browser.find_element(*self.PASSWORD_FIELD).clear()
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys("bitnami")
        self._click(self.LOGIN_BUTTON)

    def check_title(self):
        self._element(self.PANEL_TITLE)

    def enter_a_valid_username(self):
        self._click(self.USERNAME_FIELD)
        self.browser.find_element(*self.USERNAME_FIELD).clear()
        self.browser.find_element(*self.USERNAME_FIELD).send_keys("user")

    def enter_a_valid_password(self):
        self._click(self.PASSWORD_FIELD)
        self.browser.find_element(*self.PASSWORD_FIELD).clear()
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys("bitnami")

    def click_on_the_button_login(self):
        self._click(self.LOGIN_BUTTON)

    def enter_a_invalid_username(self):
        self._click(self.USERNAME_FIELD)
        self.browser.find_element(*self.USERNAME_FIELD).clear()
        self.browser.find_element(*self.USERNAME_FIELD).send_keys(fake.name())

    def enter_a_invalid_password(self):
        self._click(self.PASSWORD_FIELD)
        self.browser.find_element(*self.PASSWORD_FIELD).clear()
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(fake.password())
