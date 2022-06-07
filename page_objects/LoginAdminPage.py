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
        self.input(self.USERNAME_FIELD, "user")
        self.input(self.PASSWORD_FIELD, "bitnami")
        self._click(self.LOGIN_BUTTON)

    def check_title(self):
        self._element(self.PANEL_TITLE)

    def enter_a_valid_username(self):
        self.input(self.USERNAME_FIELD, "user")

    def enter_a_valid_password(self):
        self.input(self.PASSWORD_FIELD, "bitnami")

    def click_on_the_button_login(self):
        self._click(self.LOGIN_BUTTON)

    def enter_a_invalid_username(self):
        self.input(self.USERNAME_FIELD, fake.name())

    def enter_a_invalid_password(self):
        self.input(self.PASSWORD_FIELD, fake.password())
