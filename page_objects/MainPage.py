import random
import time
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    FIND_MY_ACCOUNT = (By.LINK_TEXT, 'My Account')
    REGISTER_BUTTON = (By.XPATH, "// a[contains(text(), 'Register')]")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Login')]")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, ".fa-caret-down")
    USD_BUTTON = (By.NAME, "USD")
    GBP_BUTTON = (By.NAME, "GBP")
    EUR_BUTTON = (By.NAME, "EUR")
    USD_ICON = (By.XPATH, "//strong[contains(text(),'$')]")
    GBP_ICON = (By.XPATH, "//strong[contains(text(),'£')]")
    EUR_ICON = (By.XPATH, "//strong[contains(text(),'€')]")
    PHONE_BUTTON = (By.CSS_SELECTOR, ".fa-phone")
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, ".fa-heart")
    SHOPPING_CART_BUTTON = (By.CSS_SELECTOR, ".fa-shopping-cart")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".fa-share")
    SEARCH_FIELD = (By.CSS_SELECTOR, ".input-lg")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-lg")
    SEARCH_TEXT = (By.XPATH, "//h2[contains(text(),'Products meeting the search criteria')]")
    SHOPPING_PREVIEW_BUTTON = (By.XPATH, "//button[@type='button' and @data-toggle='dropdown']")
    EMPTY_SHOPPING_CART_TEXT = (By.XPATH, "//p[contains(text(),'Your shopping cart is empty!')]")
    UPPER_SWIPER_BUTTON_FORWARD = (
        By.XPATH, "//div [@class='slideshow swiper-viewport']/div[3]/div[@class='swiper-button-next']")
    UPPER_SWIPER_BUTTON_BACK = (
        By.XPATH, "//div [@class='slideshow swiper-viewport']/div[3]/div[@class='swiper-button-prev']")
    PRODUCT_ITEM = (By.CSS_SELECTOR, ".product-layout")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".fa-shopping-cart")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".btn-danger")
    DESKTOPS_BUTTON = (By.LINK_TEXT, "Desktops")
    SHOW_ALL_DESKTOPS_BUTTON = (By.LINK_TEXT, "Show All Desktops")
    PC_BUTTON = (By.XPATH, "//a[contains(text(),'PC (0)')]")
    MAC_BUTTON = (By.XPATH, "//a[contains(text(),'Mac (1)')]")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    TABLETS_BUTTON = (By.LINK_TEXT, "Tablets")
    SOFTWARE_BUTTON = (By.LINK_TEXT, "Software")

    def go_to_registration(self):
        self._click(self.FIND_MY_ACCOUNT)
        self._click(self.REGISTER_BUTTON)

    def click_currency_button(self):
        self._click(self.CURRENCY_BUTTON)

    def usd_button_click(self):
        self._click(self.USD_BUTTON)

    def gbp_button_click(self):
        self._click(self.GBP_BUTTON)

    def eur_button_click(self):
        self._click(self.EUR_BUTTON)

    def usd_icon_check(self):
        self._element(self.USD_ICON)

    def gpb_icon_check(self):
        self._element(self.GBP_ICON)

    def eur_icon_check(self):
        self._element(self.EUR_ICON)

    def my_account_button_click(self):
        self._click(self.FIND_MY_ACCOUNT)

    def register_button_check(self):
        self._element(self.REGISTER_BUTTON)

    def login_button_check(self):
        self._element(self.LOGIN_BUTTON)

    def phone_button_click(self):
        self._click(self.PHONE_BUTTON)

    def wish_list_button_click(self):
        self._click(self.WISH_LIST_BUTTON)

    def shopping_cart_button_click(self):
        self._click(self.SHOPPING_CART_BUTTON)

    def checkout_button_click(self):
        self._click(self.CHECKOUT_BUTTON)

    def field_search_check(self):
        self._element(self.SEARCH_FIELD)

    def search_button_click(self):
        self._click(self.SEARCH_BUTTON)

    def search_text_check(self):
        self._element(self.SEARCH_TEXT)

    def shopping_preview_button_click(self):
        self._click(self.SHOPPING_PREVIEW_BUTTON)

    def empty_shopping_cart_text_check(self):
        self._element(self.EMPTY_SHOPPING_CART_TEXT)

    def upper_swiper_button_click(self):
        self.browser.find_element(*self.UPPER_SWIPER_BUTTON_FORWARD)

    def upper_swiper_button_back_click(self):
        self.browser.find_element(*self.UPPER_SWIPER_BUTTON_BACK)

    def product_item_click(self):
        self._elements(self.PRODUCT_ITEM)[random.randint(0, 3)].click()

    def add_to_cart_product(self):
        self._elements(self.ADD_TO_CART_BUTTON)[random.randint(2, 3)].click()
        # иначе тест падает
        time.sleep(0.5)

    def remove_product(self):
        self._click(self.SHOPPING_PREVIEW_BUTTON)
        self._click(self.DELETE_BUTTON)

    def open_section_desktops(self):
        self._click(self.DESKTOPS_BUTTON)

    def go_to_show_all_desktops(self):
        self._click(self.SHOW_ALL_DESKTOPS_BUTTON)

    def go_to_pc_section(self):
        self._click(self.PC_BUTTON)

    def go_to_mac_section(self):
        self._click(self.MAC_BUTTON)

    def go_to_tablets_section(self):
        self._click(self.TABLETS_BUTTON)

    def go_to_software_section(self):
        self._click(self.SOFTWARE_BUTTON)

    def go_to_product(self):
        self._elements(self.PRODUCT_ITEM)[2].click()
