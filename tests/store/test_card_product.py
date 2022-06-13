from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
import allure


@allure.feature("Карточка товара")
@allure.title("Проверка радио кнопок в карточке товара")
def test_apple_cinema_30_radio_buttons(browser):
    """Шаги:
    1. Перейти в карточку товара apple_cinema_30
    2. Нажать на каждый радиобаттон
    """
    MainPage(browser).go_to_product()
    ProductPage(browser).click_radio_buttons()


@allure.feature("Карточка товара")
@allure.title("Проверка чек боксов в карточке товара")
def test_apple_cinema_30_checkboxes(browser):
    """Шаги:
    1. Перейти в карточку товара apple_cinema_30
    2. Активировать все чекбоксы
    3. Деактивировать все чекбоксы
    """
    MainPage(browser).go_to_product()
    ProductPage(browser).activation_check_boxes()
    ProductPage(browser).deactivation_check_boxes()


@allure.feature("Карточка товара")
@allure.title("Проверка поля text")
def test_apple_cinema_30_text_field(browser):
    """Шаги:
    1. Перейти в карточку товара apple_cinema_30
    2. Ввести текст в поле text
    """
    MainPage(browser).go_to_product()
    ProductPage(browser).set_text_in_field_text()


@allure.feature("Карточка товара")
@allure.title("Проверка поля textarea")
def test_apple_cinema_30_textarea_field(browser):
    """Шаги:
    1. Перейти в карточку товара apple_cinema_30
    2. Ввести текст в поле textarea
    """
    MainPage(browser).go_to_product()
    ProductPage(browser).set_text_in_field_text_area()


@allure.feature("Карточка товара")
@allure.title("Проверка поля Date с выбором даты из календаря")
def test_apple_cinema_30_date(browser):
    """Шаги:
    1. Перейти в карточку товара apple_cinema_30
    2. Выбрать дату из календаря
    """
    MainPage(browser).go_to_product()
    ProductPage(browser).select_day_in_date_calendar()
