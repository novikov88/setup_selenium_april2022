import pytest

"""Для запуска теста использовать параметр --url http://192.168.1.70:8081/admin/
или заменить на свой IP"""
import allure
from page_objects.LoginAdminPage import LoginAdminPage
from page_objects.DashboardAdminPage import DashboardAdminPage
from page_objects.page_elements.SuccessAlert import SuccessAlert


@pytest.mark.admin
@allure.feature("Авторизация администратором")
@allure.title("Успешная авторизация и логаут")
def test_admin_successful_authorization(browser):
    """Шаги:
    1. Заполнить Username валидным значением
    2. Заполнить поле Password валидным значением
    3. Нажать на кнопку Login
    4. Проверить что прошла авторизация
    5. Выйти из ЛК
    6. Проверить что пользователь вышел из ЛК"""
    LoginAdminPage(browser).check_title()
    LoginAdminPage(browser).successful_authorization_by_admin()
    DashboardAdminPage(browser).navigation_panel_check()
    DashboardAdminPage(browser).logout()
    LoginAdminPage(browser).check_title()


@pytest.mark.admin
@allure.feature("Добавление нового товара")
@allure.title("Успешное добавление нового товара")
def test_add_new_product(browser):
    """Шаги:
    1. Авторизоваться админом
    2. Перейти на меню добавления товара
    3. Заполнить все необходимые поля
    4. Нажать на кнопку Save
    5. Проверить что товар добавлен"""
    LoginAdminPage(browser).successful_authorization_by_admin()
    DashboardAdminPage(browser).go_to_section_adding_product()
    DashboardAdminPage(browser).set_product_name()
    DashboardAdminPage(browser).set_description()
    DashboardAdminPage(browser).set_meta_tag()
    DashboardAdminPage(browser).go_to_data_tab()
    DashboardAdminPage(browser).set_model()
    DashboardAdminPage(browser).set_price()
    DashboardAdminPage(browser).save_product()
    DashboardAdminPage(browser).check_product()


@pytest.mark.admin
@allure.feature("Удаление товара")
@allure.title("Успешное удаление товара")
def test_delete_product(browser):
    """Шаги:
    1. Авторизоваться админом
    2. Перейти на страницу товаров
    3. Выбрать товар
    4. Удалить товар
    5. Проверить что товар удален"""
    LoginAdminPage(browser).successful_authorization_by_admin()
    DashboardAdminPage(browser).go_to_section_all_products()
    DashboardAdminPage(browser).choose_a_product()
    DashboardAdminPage(browser).delete_a_product()
    SuccessAlert(browser).check_alert()
    SuccessAlert(browser).close_alert()


@pytest.mark.admin
@allure.feature("Авторизация администратором")
@allure.title("Ошибка при авторизации с неверным паролем")
def test_admin_invalid_password(browser):
    """Шаги:
    1. Заполнить Username валидным значением
    2. Заполнить поле Password не валидным значением
    3. Нажать на кнопку Login
    4. Проверить ошибку в алерте
    5. Закрыть алерт"""
    LoginAdminPage(browser).enter_a_valid_username()
    LoginAdminPage(browser).enter_a_invalid_password()
    LoginAdminPage(browser).click_on_the_button_login()
    SuccessAlert(browser).check_alert()
    SuccessAlert(browser).close_alert()


@pytest.mark.admin
@allure.feature("Авторизация администратором")
@allure.title("Ошибка при авторизации с неверным логином")
def test_admin_invalid_login(browser):
    """Шаги:
    1. Заполнить Username не валидным значением
    2. Заполнить поле Password валидным значением
    3. Нажать на кнопку Login
    4. Проверить ошибку в алерте
    5. Закрыть алерт"""
    LoginAdminPage(browser).enter_a_invalid_username()
    LoginAdminPage(browser).enter_a_valid_password()
    LoginAdminPage(browser).click_on_the_button_login()
    SuccessAlert(browser).check_alert()
    SuccessAlert(browser).close_alert()


@pytest.mark.admin
@allure.feature("Авторизация администратором")
@allure.title("Ошибка при авторизации с неверным логином и паролем")
def test_admin_incorrect_username_and_password(browser):
    """Шаги:
    1. Заполнить Username не валидным значением
    2. Заполнить поле Password не валидным значением
    3. Нажать на кнопку Login
    4. Проверить ошибку в алерте
    5. Закрыть алерт"""
    LoginAdminPage(browser).enter_a_invalid_username()
    LoginAdminPage(browser).enter_a_invalid_password()
    LoginAdminPage(browser).click_on_the_button_login()
    SuccessAlert(browser).check_alert()
    SuccessAlert(browser).close_alert()


@pytest.mark.admin
@allure.feature("Авторизация администратором")
@allure.title("Ошибка при авторизации без заполнения логина и пароля")
def test_admin_without_username_and_password(browser):
    """Шаги:
    1. Нажать на кнопку Login не заполняя полей
    2. Проверить ошибку в алерте
    3. Закрыть алерт"""
    LoginAdminPage(browser).click_on_the_button_login()
    SuccessAlert(browser).check_alert()
    SuccessAlert(browser).close_alert()
