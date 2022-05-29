from selenium.webdriver.common.by import By


class LoginPage:
    SUCCESS_TEXT = (By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]")
    CLICK_CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    FIND_MY_ACCOUNT = (By.LINK_TEXT, 'My Account')
    CLICK_LOGOUT = (By.LINK_TEXT, 'Logout')

    def __init__(self, browser):
        self.browser = browser

    def check_registration_success(self):
        self.browser.find_element(*self.SUCCESS_TEXT)

    def logout(self):
        self.browser.find_element(*self.CLICK_CONTINUE_BUTTON).click()
        self.browser.find_element(*self.FIND_MY_ACCOUNT).click()
        self.browser.find_element(*self.CLICK_LOGOUT).click()
