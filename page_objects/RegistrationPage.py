from selenium.webdriver.common.by import By
from faker import Faker
from page_objects.BasePage import BasePage

# создаем экземпляр класса Faker для генерации данных
fake = Faker()


class RegistrationPage(BasePage):
    FIELD_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    FIELD_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#input-email")
    FIELD_PHONE = (By.CSS_SELECTOR, "#input-telephone")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    FIELD_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
    CONSENT_CHECKBOX = (By.NAME, "agree")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    RADIO_BUTTON_1 = (By.XPATH, "//label[contains(text(),'Subscribe')]/../div[1]/label[1]")
    RADIO_BUTTON_2 = (By.XPATH, "//label[contains(text(),'Subscribe')]/../div[1]/label[2]")
    PRIVACY_POLICY_BUTTON = (By.LINK_TEXT, 'Privacy Policy')
    TEXT_PRIVACY_POLICY = (By.XPATH, "//h4[contains(text(),'Privacy Policy')]")
    LOGIN_PAGE_BUTTON = (By.LINK_TEXT, 'login page')
    DANGER_TEXT = (By.CSS_SELECTOR, ".text-danger")

    def successful_registration(self):
        self.browser.find_element(*self.FIELD_FIRSTNAME).send_keys(fake.name())
        self.browser.find_element(*self.FIELD_LASTNAME).send_keys(fake.last_name())
        self.browser.find_element(*self.FIELD_EMAIL).send_keys(fake.email())
        self.browser.find_element(*self.FIELD_PHONE).send_keys(fake.phone_number())
        self.browser.find_element(*self.FIELD_PASSWORD).send_keys('123456')
        self.browser.find_element(*self.FIELD_CONFIRM_PASSWORD).send_keys('123456')
        self._click(self.CONSENT_CHECKBOX)
        self._click(self.REGISTRATION_BUTTON)

    def click_registration_button(self):
        self._click(self.REGISTRATION_BUTTON)

    def count_text_danger(self):
        text_danger = self._elements(self.DANGER_TEXT)
        return text_danger

    def enter_first_name(self):
        self.browser.find_element(*self.FIELD_FIRSTNAME).send_keys(fake.name())

    def enter_last_name(self):
        self.browser.find_element(*self.FIELD_LASTNAME).send_keys(fake.last_name())

    def enter_email(self):
        self.browser.find_element(*self.FIELD_EMAIL).send_keys(fake.email())

    def enter_phone(self):
        self.browser.find_element(*self.FIELD_PHONE).send_keys(fake.phone_number())

    def enter_password(self):
        self.browser.find_element(*self.FIELD_PASSWORD).send_keys('123456')

    def enter_confirm_password(self):
        self.browser.find_element(*self.FIELD_CONFIRM_PASSWORD).send_keys('123456')

    def click_on_radio_button_1(self):
        self._click(self.RADIO_BUTTON_1)

    def click_on_radio_button_2(self):
        self._click(self.RADIO_BUTTON_2)

    def click_on_privacy_policy(self):
        self._click(self.PRIVACY_POLICY_BUTTON)

    def check_text_privacy_policy(self):
        self._element(self.TEXT_PRIVACY_POLICY)

    def click_login_page_button(self):
        self._click(self.LOGIN_PAGE_BUTTON)
