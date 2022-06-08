from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AccountPage(BasePage):
    SUCCESS_TEXT = (By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    MY_ACCOUNT_BUTTON = (By.LINK_TEXT, 'My Account')
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Logout')

    def check_registration_success(self):
        self._element(self.SUCCESS_TEXT)

    def logout(self):
        self._click(self.CONTINUE_BUTTON)
        self._click(self.MY_ACCOUNT_BUTTON)
        self._click(self.LOGOUT_BUTTON)
