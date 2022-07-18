from page_objects.MainPage import MainPage
from page_objects.CatalogPage import CatalogPage
import allure


@allure.feature("Каталог")
@allure.title("Проверка перехода в каталог Desktops по кнопке Show All Desktops")
def test_catalog_desktops_show_all(browser):
    """Шаги:
    1. Нажать на меню Desktops и выбор Show All Desktops
    2. Проверить что открыта страница Desktops"""
    MainPage(browser).open_section_desktops()
    MainPage(browser).go_to_show_all_desktops()
    CatalogPage(browser).product_compare_check()


@allure.feature("Каталог")
@allure.title("Проверка перехода в каталог PC по кнопке PC")
def test_catalog_desktops_pc(browser):
    """Шаги:
    1. Нажать на меню Desktops и выбор PC
    2. Проверить что открыта страница PC"""
    MainPage(browser).open_section_desktops()
    MainPage(browser).go_to_pc_section()
    CatalogPage(browser).back_to_main_page()


@allure.feature("Каталог")
@allure.title("Проверка перехода в каталог Mac по кнопке Mac")
def test_catalog_desktops_mac(browser):
    """Шаги:
    1. Нажать на меню Desktops и выбор Mac
    2. Проверить что открыта страница Mac и на ней отображается минимум одна карточка товара"""
    MainPage(browser).open_section_desktops()
    MainPage(browser).go_to_mac_section()
    count_items = CatalogPage(browser).calculate_product_card()
    assert len(count_items) > 0


@allure.feature("Каталог")
@allure.title("Проверка перехода в каталог tablets по кнопке tablets")
def test_catalog_tablets(browser):
    """Шаги:
    1. Нажать на меню tablets
    2. Проверить что открыта страница tablets и на ней отображается минимум одна карточка товара"""
    MainPage(browser).go_to_tablets_section()
    count_items = CatalogPage(browser).calculate_product_card()
    assert len(count_items) > 0


@allure.feature("Каталог")
@allure.title("Проверка перехода в каталог Software")
def test_catalog_software(browser):
    """Шаги:
    1. Нажать на меню Software
    2. Проверить что открыта страница Software и на ней не отображается карточка товара
    3. Вернуться на главную страницу"""
    MainPage(browser).go_to_software_section()
    count_items = CatalogPage(browser).calculate_product_card()
    assert len(count_items) == 0
    CatalogPage(browser).back_to_main_page()
