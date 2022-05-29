from page_objects.MainPage import MainPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.AccountPage import AccountPage
from page_objects.LoginPage import LoginPage
from page_objects.page_elements.SuccessAlert import SuccessAlert


# создаем экземпляр класса Faker для генерации данных


# тест успешная регистрация и выход из ЛК
def test_successful_registration_and_logout(browser):
    """Тест проверяет успешную регистрацию пользователя"""
    # главная поиск элемента, клик и переход на страницу регистрации
    MainPage(browser).go_to_registration()
    # страница регистрации заполнение полей и нажатие на кнопку регистрации
    RegistrationPage(browser).successful_registration()
    # страница ЛК проверка наличия элементов и logout
    AccountPage(browser).check_registration_success()
    AccountPage(browser).logout()
    # страница логина проверка наличия элемента
    LoginPage(browser).check_logout_text()


def test_registration_error(browser):
    """Тест проверяет отображение текста предупреждения к обязательным полям при нажатии кнопки регистрации при
    незаполненных полях"""
    # главная поиск элемента, клик и переход на страницу регистрации
    MainPage(browser).go_to_registration()
    # страница регистрации нажатие на кнопки для проверки ошибок
    RegistrationPage(browser).click_registration_button()
    # страница регистрации проверка наличия алерта
    SuccessAlert(browser).check_alert()
    # страница регистрации проверка количества подсказок с ошибками
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 5


def test_registration_not_all_fields_1(browser):
    """Тест включает заполнение одного обязательного поля First Name и нажатие на кнопку регистрации.
    Осуществляется проверка текста предупреждения к остальным обязательным полям"""
    # главная поиск элемента, клик и переход на страницу регистрации
    MainPage(browser).go_to_registration()
    # страница регистрации заполнение полей и нажатие на кнопку регистрации
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).click_registration_button()
    # страница регистрации проверка наличия алерта
    SuccessAlert(browser).check_alert()
    # страница регистрации проверка количества ошибок
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 4


def test_registration_not_all_fields_2(browser):
    """Тест включает заполнение двух обязательных полей First Name, Last Name и нажатие на кнопку регистрации.
    Осуществляется проверка текста предупреждения к остальным обязательным полям"""
    # главная поиск элемента, клик и переход на страницу регистрации
    MainPage(browser).go_to_registration()
    # страница регистрации заполнение полей и нажатие на кнопку регистрации
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).click_registration_button()
    # страница регистрации проверка наличия алерта
    SuccessAlert(browser).check_alert()
    # страница регистрации проверка количества ошибок
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 3


def test_registration_not_all_fields_3(browser):
    """Тест включает заполнение трех обязательных полей First Name, Last Name, E-Mail и нажатие на кнопку регистрации.
    Осуществляется проверка текста предупреждения к остальным обязательным полям"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).enter_email()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 2


def test_registration_not_all_fields_4(browser):
    """Тест включает заполнение 4-х обязательных полей First Name, Last Name, E-Mail, Telephone и нажатие на кнопку
    регистрации. Осуществляется проверка текста предупреждения к остальным обязательным полям"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).enter_email()
    RegistrationPage(browser).enter_phone()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 1


def test_registration_not_all_fields_5(browser):
    """Тест включает заполнение 5-и обязательных полей First Name, Last Name, E-Mail, Telephone, Password без
    подтверждения пароля и нажатие на кнопку регистрации. Осуществляется проверка текста предупреждения к полю
    подтверждения пароля"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).enter_email()
    RegistrationPage(browser).enter_phone()
    RegistrationPage(browser).enter_password()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 1


def test_registration_not_all_fields_6(browser):
    """Тест включает заполнение всех обязательных полей, но без активации чекбокса "I have read and agree to the
    Privacy Policy ". Осуществляется проверка алерта предупреждения к чекбоксу"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).enter_email()
    RegistrationPage(browser).enter_phone()
    RegistrationPage(browser).enter_password()
    RegistrationPage(browser).enter_confirm_password()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()


def test_registration_toggle_radio_buttons(browser):
    """Тест включает проверку переключения радио кнопок Subscribe"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).click_on_radio_button_1()
    RegistrationPage(browser).click_on_radio_button_2()


def test_registration_modal_privacy_policy(browser):
    """Тест включает проверку отображения модального окна Privacy Policy"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).click_on_privacy_policy()
    RegistrationPage(browser).check_text_privacy_policy()
    SuccessAlert(browser).close_alert()


def test_registration_go_to_login_page(browser):
    """Тест включает проверку перехода на страницу login page"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).click_login_page_button()
    LoginPage(browser).check_returning_customer_text()
