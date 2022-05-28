from selenium.webdriver.common.by import By
from exception_handler import wait_element


# тесты на категорию Desktops
def test_catalog_desktops_show_all(browser):
    """Тест на каталог Desktops нажатие на кнопку Show All Desktops"""
    # главная нажатие на меню Desktops и выбор Show All Desktops
    browser.find_element(By.LINK_TEXT, "Desktops").click()
    browser.find_element(By.LINK_TEXT, "Show All Desktops").click()
    # каталог поиск элемента
    browser.find_element(By.PARTIAL_LINK_TEXT, "Product Compare (0)").click()


def test_catalog_desktops_pc(browser):
    """Тест на каталог Desktops нажатие на кнопку PC и проверка элемента на страницы"""
    # главная нажатие на меню Desktops и выбор PC
    browser.find_element(By.LINK_TEXT, "Desktops").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'PC (0)')]").click()
    # каталог поиск элемента
    browser.find_element(By.XPATH, "//h2[contains(text(),'PC')]")


def test_catalog_desktops_mac(browser):
    """Тест на каталог Desktops нажатие на кнопку Mac и проверка элемента Mac на страницы"""
    # главная нажатие на меню Desktops и выбор Mac
    browser.find_element(By.LINK_TEXT, "Desktops").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'Mac (1)')]").click()
    # каталог поиск элемента
    browser.find_element(By.XPATH, "//h2[contains(text(),'Mac')]")


# тесты на категорию Show All Laptops & Notebooks
def test_catalog_desktops_laptops(browser):
    """Тест на каталог Desktops нажатие на кнопку Show All Laptops & Notebooks"""
    # главная нажатие на меню Show All Laptops & Notebooks и выбор Laptops & Notebooks
    browser.find_element(By.LINK_TEXT, "Laptops & Notebooks").click()
    browser.find_element(By.LINK_TEXT, "Show All Laptops & Notebooks").click()
    # каталог поиск элемента
    wait_element(browser, (By.XPATH, "//p[contains(text(),'Shop Laptop feature only the best laptop deals on ')]"))


def test_catalog_macs(browser):
    """Тест на каталог Desktops нажатие на кнопку Macs и проверка элемента на страницы"""
    # главная нажатие на меню Show All Laptops & Notebooks и выбор Macs
    browser.find_element(By.LINK_TEXT, "Laptops & Notebooks").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'Macs (0)')]").click()
    # каталог поиск элемента и нажатие на кнопку Continue
    browser.find_element(By.XPATH, "//p[contains(text(),'There are no products to list in this category.')]")
    browser.find_element(By.XPATH, "// a[contains(text(), 'Continue')]").click()


def test_catalog_windows(browser):
    """Тест на каталог Desktops нажатие на кнопку Windows и проверка элемента на страницы"""
    # главная нажатие на меню Show All Laptops & Notebooks и выбор Windows
    browser.find_element(By.LINK_TEXT, "Laptops & Notebooks").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'Windows (0)')]").click()
    # каталог поиск элемента и нажатие на кнопку Continue
    browser.find_element(By.XPATH, "//h2[contains(text(),'Windows')]")
    browser.find_element(By.XPATH, "// a[contains(text(), 'Continue')]").click()


# тесты на категорию Components
def test_catalog_components(browser):
    """Проверка наличия элементов во вкладке Components"""
    # главная нажатие на меню Components
    browser.find_element(By.LINK_TEXT, "Components").click()
    # главная поиск элементов
    browser.find_element(By.XPATH, "//a[contains(text(),'Mice and Trackballs (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'Monitors (2)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'Printers (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'Scanners (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'Web Cameras (0)')]")
    # главная клик по элементу Show All Components
    browser.find_element(By.LINK_TEXT, "Show All Components").click()
    # каталог поиск элементов
    browser.find_element(By.LINK_TEXT, "Mice and Trackballs (0)")
    browser.find_element(By.LINK_TEXT, "Monitors (2)")
    browser.find_element(By.LINK_TEXT, "Printers (0)")
    browser.find_element(By.LINK_TEXT, "Scanners (0)")
    browser.find_element(By.LINK_TEXT, "Web Cameras (0)")


def test_catalog_tablets(browser):
    """Проверка перехода на страницу tablets из каталога"""
    # главная нажатие на меню tablets
    browser.find_element(By.LINK_TEXT, "Tablets").click()
    # каталог поиск элементов
    wait_element(browser, (By.XPATH, "//div[contains(text(),'Showing 1 to 1 of 1 (1 Pages)')]"))
    browser.find_element(By.CSS_SELECTOR, "#list-view").click()


# тесты на категорию Software
def test_catalog_software(browser):
    """Проверка перехода на страницу Software из каталога"""
    # главная нажатие на меню Software
    browser.find_element(By.LINK_TEXT, "Software").click()
    # каталог поиск элементов
    browser.find_element(By.XPATH, "//h2[contains(text(),'Software')]")
    browser.find_element(By.XPATH, "//p[contains(text(),'There are no products to list in this category.')]")
    # каталог нажатие на кнопку Continue
    browser.find_element(By.XPATH, "// a[contains(text(), 'Continue')]").click()


# тесты на категорию Phones & PDAs
def test_catalog_phones(browser):
    """Проверка перехода на страницу Phones & PDAs из каталога"""
    # главная нажатие на меню Phones & PDAs
    browser.find_element(By.LINK_TEXT, "Phones & PDAs").click()
    # каталог поиск элементов и клик в элемент
    browser.find_element(By.XPATH, "//div[contains(text(),'Showing 1 to 3 of 3 (1 Pages)')]")
    browser.find_element(By.LINK_TEXT, "HTC Touch HD").click()
    # карточка товара поиск элемента
    browser.find_element(By.XPATH, "//p[contains(text(),'HTC Touch - in High Definition. Watch music videos')]")


# тесты на категорию Cameras
def test_catalog_cameras(browser):
    """Проверка перехода на страницу Cameras из каталога"""
    # главная нажатие на меню Cameras
    browser.find_element(By.LINK_TEXT, "Cameras").click()
    # каталог поиск элемента и клик в элемент
    browser.find_element(By.XPATH, "//div[contains(text(),'Showing 1 to 2 of 2 (1 Pages)')]")
    browser.find_element(By.LINK_TEXT, "Nikon D300").click()
    # карточка товара поиск элемента и клик в элемент
    browser.find_element(By.LINK_TEXT, "Reviews (0)").click()
    browser.find_element(By.XPATH, "//h2[contains(text(),'Write a review')]")
    # карточка товара нажатие на кнопку
    wait_element(browser, (By.CSS_SELECTOR, "#button-review")).click()
    # карточка товара проверка алерта
    browser.find_element(By.CSS_SELECTOR, ".alert-dismissible")


# тесты на категорию MP3 Players
def test_catalog_mp3_players(browser):
    """Проверка наличия элементов во вкладке MP3 Players"""
    # главная нажатие на меню MP3 Players поиск элементов
    browser.find_element(By.LINK_TEXT, "MP3 Players").click()
    browser.find_element(By.XPATH, "//a[contains(text(),'test 11 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 12 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 15 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 16 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 17 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 18 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 19 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 20 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 21 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 22 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 23 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 24 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 4 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 5 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 6 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 7 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 8 (0)')]")
    browser.find_element(By.XPATH, "//a[contains(text(),'test 9 (0)')]")
    # главная клик по элементу
    browser.find_element(By.LINK_TEXT, "Show All MP3 Players").click()
