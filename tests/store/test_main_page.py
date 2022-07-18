from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.page_elements.SuccessAlert import SuccessAlert
import allure


@allure.feature("Смена валюты")
@allure.title("Проверка смены валюты")
def test_button_currency(browser):
    """Шаги:
    1. Кликнуть в dropdown выбора валюты и выбрать доллар
    2. Проверить в шапке, что отображается валюта = доллар
    3. Кликнуть в dropdown выбора валюты и выбрать фунты
    4. Проверить в шапке, что отображается валюта = фунт
    5. Кликнуть в dropdown выбора валюты и выбрать евро
    6. Проверить в шапке, что отображается валюта = евро
    """
    MainPage(browser).click_currency_button()
    MainPage(browser).usd_button_click()
    MainPage(browser).usd_icon_check()
    MainPage(browser).click_currency_button()
    MainPage(browser).gbp_button_click()
    MainPage(browser).gpb_icon_check()
    MainPage(browser).click_currency_button()
    MainPage(browser).eur_button_click()
    MainPage(browser).eur_icon_check()


@allure.feature("Главная / меню")
@allure.title("Проверка меню My account")
def test_button_register(browser):
    """Шаги:
    1. Нажать на My account
    2. Проверить наличия кнопки register
    3. Проверить наличия кнопки login
    """
    MainPage(browser).my_account_button_click()
    MainPage(browser).register_button_check()
    MainPage(browser).login_button_check()


@allure.feature("Главная / меню")
@allure.title("Проверка меню button phone")
def test_button_phone(browser):
    """Шаги:
    1. Проверить наличия кнопки phone"""
    MainPage(browser).phone_button_click()


@allure.feature("Главная / меню")
@allure.title("Проверка меню button wish_list")
def test_button_heart(browser):
    """Шаги:
    1. Проверить наличия кнопки wish_list"""
    MainPage(browser).wish_list_button_click()


@allure.feature("Главная / меню")
@allure.title("Проверка меню button shopping_cart")
def test_button_shopping_cart(browser):
    """Шаги:
    1. Проверить наличия кнопки shopping_cart"""
    MainPage(browser).shopping_cart_button_click()


@allure.feature("Главная / меню")
@allure.title("Проверка меню button checkout")
def test_button_share(browser):
    """Шаги:
    1. Проверить наличия кнопки checkout"""
    MainPage(browser).checkout_button_click()


@allure.feature("Главная / поиск")
@allure.title("Поиск элемента  field_search")
def test_search_panel(browser):
    """Шаги:
    1. Найти поле field_search"""
    MainPage(browser).field_search_check()


@allure.feature("Главная / поиск")
@allure.title("Поиск элемента и клик по кнопке search_button")
def test_button_search(browser):
    """Шаги:
    1. Найти и кликнуть по кнопке search_button"""
    MainPage(browser).search_button_click()
    MainPage(browser).search_text_check()


@allure.feature("Главная / корзина")
@allure.title("Поиск элемента, клик по корзине и проверка текста")
def test_shopping_preview_button(browser):
    """Шаги:
    1. Найти и кликнуть по кнопке hopping_preview_button
    2. Проверить что отображается текст '"'Your shopping cart is empty!'"""
    MainPage(browser).shopping_preview_button_click()
    MainPage(browser).empty_shopping_cart_text_check()


@allure.feature("Главная / карусель изображений")
@allure.title("Проверка кнопки пролистывания вперед")
def test_upper_swiper_button(browser):
    """Шаги:
    1. Найти и кликнуть по кнопке upper_swiper_button"""
    MainPage(browser).upper_swiper_button_click()


@allure.feature("Главная / карусель изображений")
@allure.title("Проверка кнопки пролистывания назад")
def test_upper_swiper_button_back(browser):
    """Шаги:
    1. Найти и кликнуть по кнопке upper_swiper_button_back"""
    MainPage(browser).upper_swiper_button_back_click()


@allure.feature("Главная / featured")
@allure.title("Проверка кнопки перехода в карточку товара")
def test_transition_to_goods(browser):
    """Шаги:
    1. Найти товар в блоке featured и кликнуть на него
    2. Проверить что осуществлен переход в карточку товара"""
    MainPage(browser).product_item_click()
    ProductPage(browser).add_to_cart_button_click()


@allure.feature("Главная / корзина")
@allure.title("Проверка добавления и удаления товара из корзины")
def test_add_to_cart_button(browser):
    """Шаги:
    1. Найти товар в блоке featured и добавить его [Add to card]
    2. Открыть корзину и проверить что товар добавлен
    3. Удалить товар из корзины
    4. Проверить наличие алерта
    5. Закрыть алерт"""
    MainPage(browser).add_to_cart_product()
    MainPage(browser).remove_product()
    SuccessAlert(browser).check_alert_success()
    SuccessAlert(browser).close_alert()
