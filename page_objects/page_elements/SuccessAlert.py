from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class SuccessAlert(BasePage):
    ALERT_DISMISSIBLE = (By.CSS_SELECTOR, ".alert-dismissible")
    BUTTON_X = (By.XPATH, "//button[contains(text(),'×')]")
    ALERT_SUCCESS = (By.XPATH, "//body/div[@id='common-home']/div[1]")

    def check_alert(self):
        self._element(self.ALERT_DISMISSIBLE)

    def close_alert(self):
        self._element(self.BUTTON_X)

    def check_alert_success(self):
        self._element(self.ALERT_SUCCESS)
