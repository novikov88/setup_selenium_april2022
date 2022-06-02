from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.page_elements.SuccessAlert import SuccessAlert


def test_button_currency(browser):
    """Проверка выбора валюты"""
    # главная смена валюты
    MainPage(browser).click_currency_button()
    MainPage(browser).usd_button_click()
    MainPage(browser).usd_icon_check()
    MainPage(browser).click_currency_button()
    MainPage(browser).gbp_button_click()
    MainPage(browser).gpb_icon_check()
    MainPage(browser).click_currency_button()
    MainPage(browser).eur_button_click()
    MainPage(browser).eur_icon_check()


def test_button_register(browser):
    """Проверка меню в шапке"""
    # главная поиск элемента и клик по кнопке
    MainPage(browser).my_account_button_click()
    MainPage(browser).register_button_check()
    MainPage(browser).login_button_check()


def test_button_phone(browser):
    """Проверка меню в шапке button phone"""
    # главная поиск элемента и клик по кнопке
    MainPage(browser).phone_button_click()


def test_button_heart(browser):
    """Проверка меню в шапке"""
    # главная поиск элемента и клик по кнопке
    MainPage(browser).wish_list_button_click()


def test_button_shopping_cart(browser):
    # главная поиск элемента и клик по кнопке
    MainPage(browser).shopping_cart_button_click()


def test_button_share(browser):
    """Проверка меню в шапке"""
    # главная поиск элемента и клик по кнопке
    MainPage(browser).checkout_button_click()


def test_search_panel(browser):
    """Проверка field search"""
    # главная поиск элемента и клик по кнопке
    MainPage(browser).field_search_check()


def test_button_search(browser):
    """Проверка кнопки поиска"""
    # главная поиск элемента и клик по кнопке Search
    MainPage(browser).search_button_click()
    MainPage(browser).search_text_check()


def test_shopping_preview_button(browser):
    # главная поиск элемента и клик по кнопке корзины и проверка текста
    MainPage(browser).shopping_preview_button_click()
    MainPage(browser).empty_shopping_cart_text_check()


def test_upper_swiper_button(browser):
    """Проверка кнопки вперед прокрутки изображения"""
    # главная поиск элемента и нажатие на кнопку
    MainPage(browser).upper_swiper_button_click()


def test_upper_swiper_button_back(browser):
    """Проверка кнопки назад прокрутки изображения"""
    # главная поиск элемента и нажатие на кнопку
    MainPage(browser).upper_swiper_button_back_click()


def test_transition_to_goods(browser):
    """Проверка перехода на товар с главной через блок featured"""
    # главная поиск элемента и нажатие товар
    MainPage(browser).product_item_click()
    ProductPage(browser).add_to_cart_button_click()


def test_add_to_cart_button(browser):
    """Проверка добавления товара в корзину"""
    # главная поиск элемента и нажатие кнопку добавления в корзину
    MainPage(browser).add_to_cart_product()
    # главная открытие корзины и удаление товара
    MainPage(browser).remove_product()
    # главная проверка наличия алерта и его закрытие
    SuccessAlert(browser).check_alert_success()
    SuccessAlert(browser).close_alert()
