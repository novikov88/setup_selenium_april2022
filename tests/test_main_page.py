from selenium.webdriver.common.by import By
from exception_handler import wait_element


def test_check_title(browser):
    assert "Your Store" == browser.title


def test_button_currency(browser):
    browser.find_element(By.CSS_SELECTOR, ".fa-caret-down").click()
    wait_element(browser, (By.NAME, "EUR")).click()


def test_button_register(browser):
    browser.find_element(By.CSS_SELECTOR, ".fa-user").click()
    wait_element(browser, (By.XPATH, "//a[contains(text(),'Login')]")).click()


def test_button_phone(browser):
    browser.find_element(By.CSS_SELECTOR, ".fa-phone").click()


def test_button_heart(browser):
    browser.find_element(By.CSS_SELECTOR, ".fa-heart").click()


def test_button_shopping_cart(browser):
    browser.find_element(By.CSS_SELECTOR, ".fa-shopping-cart").click()


def test_button_share(browser):
    browser.find_element(By.CSS_SELECTOR, ".fa-share").click()


def test_search_panel(browser):
    browser.find_element(By.CSS_SELECTOR, ".input-lg").click()


def test_button_search(browser):
    browser.find_element(By.CSS_SELECTOR, ".btn-lg").click()
    wait_element(browser, (By.XPATH, "//a[contains(text(),'Search')]")).click()


def test_search_panel(browser):
    browser.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    wait_element(browser, (By.XPATH, "//p[contains(text(),'Your shopping cart is empty!')]"))
