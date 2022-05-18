from selenium.webdriver.common.by import By


def test_check_title(browser):
    """Проверка title страницы"""
    assert "Your Store" == browser.title


def test_button_currency(browser):
    """Проверка выбора валюты"""
    browser.find_element(By.CSS_SELECTOR, ".fa-caret-down").click()
    browser.find_element(By.NAME, "USD").click()


def test_button_register(browser):
    """Проверка меню в шапке"""
    browser.find_element(By.CSS_SELECTOR, ".fa-user").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()


def test_button_phone(browser):
    """Проверка меню в шапке"""
    browser.find_element(By.CSS_SELECTOR, ".fa-phone").click()


def test_button_heart(browser):
    """Проверка меню в шапке"""
    browser.find_element(By.CSS_SELECTOR, ".fa-heart").click()


def test_button_shopping_cart(browser):
    browser.find_element(By.CSS_SELECTOR, ".fa-shopping-cart").click()


def test_button_share(browser):
    """Проверка меню в шапке"""
    browser.find_element(By.CSS_SELECTOR, ".fa-share").click()


def test_search_panel(browser):
    """Проверка меню в шапке"""
    browser.find_element(By.CSS_SELECTOR, ".input-lg").click()


def test_button_search(browser):
    """Проверка кнопки поиска"""
    browser.find_element(By.CSS_SELECTOR, ".btn-lg").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()


def test_shopping_preview_button(browser):
    browser.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    browser.find_element(By.XPATH, "//p[contains(text(),'Your shopping cart is empty!')]").click()


def test_upper_swiper_button(browser):
    """Проверка кнопки вперед прокрутки изображения"""
    browser.find_element(By.XPATH,
                         "//div [@class='slideshow swiper-viewport']/div[3]/"
                         "div[@class='swiper-button-next']").click()


def test_upper_swiper_button_back(browser):
    """Проверка кнопки назад прокрутки изображения"""
    browser.find_element(By.XPATH,
                         "//div [@class='slideshow swiper-viewport']/div[3]/"
                         "div[@class='swiper-button-prev']").click()


def test_transition_to_commodity_iPhone6(browser):
    """Проверка элемента iPhone6 что на него можно нажать"""
    browser.find_element(By.XPATH,
                         "//img[@class='img-responsive' and contains(@src, '192.168.1.65:8081/image/"
                         "cache/catalog/demo/banners/iPhone6-1140x380.jpg')]").click()


def test_add_to_cart_button(browser):
    """Проверка добавления товара в корзину"""
    browser.find_element(By.XPATH, "//span[contains(text(),'Ex Tax: $500.00')]/../../../div[3]/button[1]").click()
    browser.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    browser.find_element(By.CSS_SELECTOR, ".btn-danger").click()
    browser.find_element(By.XPATH, "//body/div[@id='common-home']/div[1]")
    browser.find_element(By.XPATH, "//button[contains(text(),'×')]").click()
