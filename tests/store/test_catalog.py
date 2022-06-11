from page_objects.MainPage import MainPage
from page_objects.CatalogPage import CatalogPage


def test_catalog_desktops_show_all(browser):
    """Тест на каталог Desktops нажатие на кнопку Show All Desktops"""
    # главная нажатие на меню Desktops и выбор Show All Desktops
    MainPage(browser).open_section_desktops()
    MainPage(browser).go_to_show_all_desktops()
    # каталог поиск элемента
    CatalogPage(browser).product_compare_check()


def test_catalog_desktops_pc(browser):
    """Тест на каталог Desktops нажатие на кнопку PC и проверка элемента на страницы"""
    # главная нажатие на меню Desktops и выбор PC
    MainPage(browser).open_section_desktops()
    MainPage(browser).go_to_pc_section()
    CatalogPage(browser).back_to_main_page()


def test_catalog_desktops_mac(browser):
    """Тест на каталог Desktops нажатие на кнопку Mac и проверка элемента Mac на страницы"""
    # главная нажатие на меню Desktops и выбор Mac
    MainPage(browser).open_section_desktops()
    MainPage(browser).go_to_mac_section()
    # каталог поиск элемента
    count_items = CatalogPage(browser).calculate_product_card()
    assert len(count_items) > 0


def test_catalog_tablets(browser):
    """Проверка перехода на страницу tablets из каталога"""
    # главная нажатие на меню tablets
    MainPage(browser).go_to_tablets_section()
    count_items = CatalogPage(browser).calculate_product_card()
    assert len(count_items) > 0


# тесты на категорию Software
def test_catalog_software(browser):
    """Проверка перехода на страницу Software из каталога"""
    # главная нажатие на меню Software
    MainPage(browser).go_to_software_section()
    count_items = CatalogPage(browser).calculate_product_card()
    assert len(count_items) == 0
    CatalogPage(browser).back_to_main_page()
