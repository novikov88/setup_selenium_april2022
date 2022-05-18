from selenium.webdriver.common.by import By
from exception_handler import wait_element
from faker import Faker

# создаем экземпляр класса Faker для генерации данных
fake = Faker()


# тесты на карточку товара проверка радиобаттонов
def test_apple_cinema_30_radiobuttons(browser):
    """тесты на карточку товара проверка радиобаттонов"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.XPATH, "//div[@id='input-option218']/div[1]/label").click()
    browser.find_element(By.XPATH, "//div[@id='input-option218']/div[2]/label").click()
    browser.find_element(By.XPATH, "//div[@id='input-option218']/div[3]/label").click()


# тесты на карточку товара проверка чекбоксов
def test_apple_cinema_30_checkboxes(browser):
    """тесты на карточку товара проверка чекбоксов"""
    # активация чекбоксов
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.XPATH, "//div[@id='input-option223']/div[1]/label").click()
    browser.find_element(By.XPATH, "//div[@id='input-option223']/div[2]/label").click()
    browser.find_element(By.XPATH, "//div[@id='input-option223']/div[3]/label").click()
    browser.find_element(By.XPATH, "//div[@id='input-option223']/div[4]/label").click()
    # деактивация чекбоксов
    browser.find_element(By.XPATH, "//div[@id='input-option223']/div[1]/label").click()
    browser.find_element(By.XPATH, "//div[@id='input-option223']/div[2]/label").click()
    browser.find_element(By.XPATH, "//div[@id='input-option223']/div[3]/label").click()
    browser.find_element(By.XPATH, "//div[@id='input-option223']/div[4]/label").click()


# тесты на карточку товара проверка поля текст
def test_apple_cinema_30_text_field(browser):
    """тесты на карточку товара проверка поля текст"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    # отчищаем поле от дефолтного текста
    browser.find_element(By.XPATH, "//input[@id='input-option208']").clear()
    # вводим текст Hello, world!
    browser.find_element(By.XPATH, "//input[@id='input-option208']").send_keys(fake.text())


# проверка дропдауна Select с выбором одного из значений
def test_apple_cinema_30_select_field(browser):
    """проверка дропдауна Select с выбором одного из значений"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, "#input-option217").click()
    browser.find_element(By.XPATH, "//option[contains(text(),'(+$4.80)')]").click()

    browser.find_element(By.CSS_SELECTOR, "#input-option217").click()
    browser.find_element(By.XPATH, "//option[contains(text(),'(+$3.60)')]").click()

    browser.find_element(By.CSS_SELECTOR, "#input-option217").click()
    browser.find_element(By.XPATH, "//option[contains(text(),'(+$1.20)')]").click()

    browser.find_element(By.CSS_SELECTOR, "#input-option217").click()
    browser.find_element(By.XPATH, "//option[contains(text(),'(+$2.40)')]").click()


# проверка поля textarea с вводом текста
def test_apple_cinema_30_textarea_field(browser):
    """проверка поля textarea с вводом текста"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, '#input-option209').send_keys(fake.text())


#  проверка кнопки Upload File
def test_apple_cinema_30_upload_button(browser):
    """проверка кнопки Upload File"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, '#button-upload222').click()


#  проверка поля Date с выбором даты из календаря
def test_apple_cinema_30_date(browser):
    """проверка поля Date с выбором даты из календаря"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, '.fa-calendar').click()
    browser.find_element(By.XPATH, '//tbody/tr[2]/td').click()


#  проверка поля Date с вводом времени
def test_apple_cinema_30_time(browser):
    """проверка поля Date с вводом времени"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, '#input-option221').clear()
    browser.find_element(By.CSS_SELECTOR, '#input-option221').send_keys('23:59')
    browser.find_element(By.XPATH, "//body").click()


#  проверка поля Date & Time с вводом даты и времени
def test_apple_cinema_30_data_time(browser):
    """проверка поля Date & Time с вводом даты и времени"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, '#input-option220').clear()
    browser.find_element(By.CSS_SELECTOR, '#input-option220').send_keys('2020-05-15 15:15')
    browser.find_element(By.XPATH, "//body").click()


#  проверка поля Qty с вводом значения
def test_apple_cinema_30_qty(browser):
    """проверка поля Qty с вводом значения"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, '#input-quantity').clear()
    browser.find_element(By.CSS_SELECTOR, '#input-quantity').send_keys('+100500')
    browser.find_element(By.XPATH, "//body").click()


#  поиск кнопки Add to Cart с проверкой сообщений об обязательности полей после нажатия
def test_apple_cinema_30_add_to_cart(browser):
    """поиск кнопки Add to Cart с проверкой сообщений об обязательности полей после нажатия"""
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, '#button-cart').click()
    # ожидание
    wait_element(browser, (By.XPATH, "//div[contains(text(),'Textarea required!')]"))
    # ищем через find_element так как ожидание уже прошло в строчке выше
    browser.find_element(By.XPATH, "//div[contains(text(),'Radio required!')]")
    browser.find_element(By.XPATH, "//div[contains(text(),'Checkbox required!')]")
    browser.find_element(By.XPATH, "//div[contains(text(),'Select required!')]")
    browser.find_element(By.XPATH, "//div[contains(text(),'File required!')]")
