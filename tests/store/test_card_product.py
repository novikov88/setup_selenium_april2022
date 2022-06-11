from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage


# тесты на карточку товара проверка радиобаттонов
def test_apple_cinema_30_radio_buttons(browser):
    """Тесты на карточку товара проверка радиобаттонов"""
    # главная страница переход в карточку товара
    MainPage(browser).go_to_product()
    # страница продукта клики по радиобаттонам
    ProductPage(browser).click_radio_buttons()


# тесты на карточку товара проверка чекбоксов
def test_apple_cinema_30_checkboxes(browser):
    """Тесты на карточку товара проверка чекбоксов"""
    # главная страница переход в карточку товара
    MainPage(browser).go_to_product()
    # страница продукта активация чекбоксов
    ProductPage(browser).activation_check_boxes()
    # страница продукта деактивация чекбоксов
    ProductPage(browser).deactivation_check_boxes()


# тесты на карточку товара проверка поля текст
def test_apple_cinema_30_text_field(browser):
    """Тесты на карточку товара проверка поля текст"""
    # главная страница переход в карточку товара
    MainPage(browser).go_to_product()
    # карточка товара ввод текста в поле "Текст"
    ProductPage(browser).set_text_in_field_text()


# проверка поля textarea с вводом текста
def test_apple_cinema_30_textarea_field(browser):
    """Проверка поля textarea с вводом текста"""
    # главная страница переход в карточку товара
    MainPage(browser).go_to_product()
    # карточка товара ввод текста в поле "Textarea"
    ProductPage(browser).set_text_in_field_text_area()


#  проверка поля Date с выбором даты из календаря
def test_apple_cinema_30_date(browser):
    """Проверка поля Date с выбором даты из календаря"""
    # главная страница переход в карточку товара
    MainPage(browser).go_to_product()
    # карточка товара ввод даты из календаря
    ProductPage(browser).select_day_in_date_calendar()
