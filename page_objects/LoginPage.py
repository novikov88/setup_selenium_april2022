from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    TEXT_LOGOUT = (By.XPATH, "//h1[contains(text(),'Account Logout')]")
    TEXT_RETURNING_CUSTOMER = (By.XPATH, "//h2[contains(text(),'Returning Customer')]")

    def check_logout_text(self):
        self._click(self.TEXT_LOGOUT)

    def check_returning_customer_text(self):
        self._elements(self.TEXT_RETURNING_CUSTOMER)
