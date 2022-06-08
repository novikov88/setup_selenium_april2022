"""Для запуска теста использовать параметр --url http://192.168.1.65:8081/admin/
или заменить на свой IP"""

from page_objects.LoginAdminPage import LoginAdminPage
from page_objects.DashboardAdminPage import DashboardAdminPage
from page_objects.page_elements.SuccessAlert import SuccessAlert


def test_admin_successful_authorization(browser):
    """Тест проверяет успешную авторизацию администратора и выход и админки"""
    # поиск элемента на странице логина в админке
    LoginAdminPage(browser).check_title()
    # авторизация админом страница логина
    LoginAdminPage(browser).successful_authorization_by_admin()
    # поиск элемента на странице dashboard
    DashboardAdminPage(browser).navigation_panel_check()
    # logout из dashboard
    DashboardAdminPage(browser).logout()
    # поиск элемента на странице логина в админке
    LoginAdminPage(browser).check_title()


def test_add_new_product(browser):
    """Тест проверяет успешное добавление товара в админке"""
    # авторизация админом страница логина
    LoginAdminPage(browser).successful_authorization_by_admin()
    # перейти к добавлению товара
    DashboardAdminPage(browser).go_to_section_adding_product()
    DashboardAdminPage(browser).set_product_name()
    DashboardAdminPage(browser).set_description()
    DashboardAdminPage(browser).set_meta_tag()
    DashboardAdminPage(browser).go_to_data_tab()
    DashboardAdminPage(browser).set_model()
    DashboardAdminPage(browser).set_price()
    DashboardAdminPage(browser).save_product()
    DashboardAdminPage(browser).check_product()


def test_delete_product(browser):
    """Тест проверяет удаление товара в админке"""
    # авторизация админом страница логина
    LoginAdminPage(browser).successful_authorization_by_admin()
    # перейти ко всем товарам
    DashboardAdminPage(browser).go_to_section_all_products()
    # выбрать товар
    DashboardAdminPage(browser).choose_a_product()
    # удалить товар
    DashboardAdminPage(browser).delete_a_product()
    # проверка алерта с ошибкой
    SuccessAlert(browser).check_alert()
    # закрытие алерта
    SuccessAlert(browser).close_alert()


def test_admin_invalid_password(browser):
    """Тест проверяет попытку авторизации администратора с неверным паролем проверку отображения предупреждения и
    закрытие сообщения"""
    # авторизация админом страница логина
    LoginAdminPage(browser).enter_a_valid_username()
    LoginAdminPage(browser).enter_a_invalid_password()
    LoginAdminPage(browser).click_on_the_button_login()
    # проверка алерта с ошибкой
    SuccessAlert(browser).check_alert()
    # закрытие алерта
    SuccessAlert(browser).close_alert()


def test_admin_invalid_login(browser):
    """Тест проверяет попытку авторизации администратора с неверным логином проверку отображения предупреждения и
    закрытие сообщения"""
    # авторизация админом страница логина
    LoginAdminPage(browser).enter_a_invalid_username()
    LoginAdminPage(browser).enter_a_valid_password()
    LoginAdminPage(browser).click_on_the_button_login()
    # проверка алерта с ошибкой
    SuccessAlert(browser).check_alert()
    # закрытие алерта
    SuccessAlert(browser).close_alert()


def test_admin_incorrect_username_and_password(browser):
    """Тест проверяет попытку авторизации администратора с неверным логином и паролем, проверку отображения
    предупреждения и закрытие сообщения"""
    # авторизация админом страница логина
    LoginAdminPage(browser).enter_a_invalid_username()
    LoginAdminPage(browser).enter_a_invalid_password()
    LoginAdminPage(browser).click_on_the_button_login()
    # проверка алерта с ошибкой
    SuccessAlert(browser).check_alert()
    # закрытие алерта
    SuccessAlert(browser).close_alert()


def test_admin_without_username_and_password(browser):
    """Тест проверяет попытку авторизации администратора без ввода логина и пароля, проверку отображения
    предупреждения и закрытие сообщения"""
    # авторизация админом страница логина
    LoginAdminPage(browser).click_on_the_button_login()
    # проверка алерта с ошибкой
    SuccessAlert(browser).check_alert()
    # закрытие алерта
    SuccessAlert(browser).close_alert()
