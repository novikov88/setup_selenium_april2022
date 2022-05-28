"""Для запуска теста использовать параметр --url http://192.168.1.65:8081/admin/
или заменить на свой IP"""
from selenium.webdriver.common.by import By
from exception_handler import *
from faker import Faker

# создаем экземпляр класса Faker для генерации данных
fake = Faker()


def test_admin_successful_login(browser):
    """Тест проверяет успешную авторизацию администратора и выход и админки"""
    # поиск элемента на странице логина в админке
    browser.find_element(By.CSS_SELECTOR, ".panel-title")
    # авторизация админом страница логина
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("user")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # поиск элемента на странице dashboard
    wait_element(browser, (By.CSS_SELECTOR, "#navigation"))
    # вылогинивание из dashboard
    browser.find_element(By.XPATH, "//span[contains(text(),'Logout')]").click()
    # поиск элемента на странице логина в админке
    browser.find_element(By.CSS_SELECTOR, ".panel-title")


def test_admin_invalid_password(browser):
    """Тест проверяет попытку авторизации администратора с неверным паролем проверку отображения предупреждения и
    закрытие сообщения"""
    # авторизация админом страница логина
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("user")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(fake.password())
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # проверка алерта с ошибкой
    browser.find_element(By.CSS_SELECTOR, ".alert-danger")
    # закрытие алерта
    browser.find_element(By.XPATH, "//button[contains(text(),'×')]").click()


def test_admin_invalid_login(browser):
    """Тест проверяет попытку авторизации администратора с неверным логином проверку отображения предупреждения и
    закрытие сообщения"""
    # авторизация админом страница логина
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # проверка алерта с ошибкой
    browser.find_element(By.CSS_SELECTOR, ".alert-danger")
    # закрытие алерта
    browser.find_element(By.XPATH, "//button[contains(text(),'×')]").click()


def test_admin_incorrect_username_and_password(browser):
    """Тест проверяет попытку авторизации администратора с неверным логином и паролем, проверку отображения
    предупреждения и закрытие сообщения"""
    # авторизация админом страница логина
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(fake.password())
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # проверка алерта с ошибкой
    browser.find_element(By.CSS_SELECTOR, ".alert-danger")
    # закрытие алерта
    browser.find_element(By.XPATH, "//button[contains(text(),'×')]").click()


def test_admin_without_username_and_password(browser):
    """Тест проверяет попытку авторизации администратора без ввода логина и пароля, проверку отображения
    предупреждения и закрытие сообщения"""
    # авторизация админом страница логина
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # проверка алерта с ошибкой
    browser.find_element(By.CSS_SELECTOR, ".alert-danger")
    # закрытие алерта
    browser.find_element(By.XPATH, "//button[contains(text(),'×')]").click()


def test_admin_forgotten_password(browser):
    """Тест проверяет кнопку восстановления пароля (forgotten password), попытку восстановить пароль на несуществующий
    email, проверку отображения ошибки, закрытие сообщения и возврат на страницу логина"""
    # страница логина нажатие на восстановление пароля
    browser.find_element(By.XPATH, "//a[contains(text(),'Forgotten Password')]").click()
    # ожидание элемента и ввод email
    wait_element(browser, (By.XPATH, "//input[@id='input-email']")).send_keys(fake.email())
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    # проверка алерта с ошибкой
    browser.find_element(By.CSS_SELECTOR, ".alert-danger")
    browser.find_element(By.XPATH, "//button[contains(text(),'×')]").click()
    # закрытие алерта
    browser.find_element(By.CSS_SELECTOR, ".fa-reply").click()
    # поиск элемента на странице логина в админке
    browser.find_element(By.CSS_SELECTOR, ".panel-title")
