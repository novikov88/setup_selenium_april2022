import allure
from page_objects.MainPage import MainPage
from page_objects.RegistrationPage import RegistrationPage
from page_objects.AccountPage import AccountPage
from page_objects.LoginPage import LoginPage
from page_objects.page_elements.SuccessAlert import SuccessAlert


@allure.feature("Регистрация пользователя")
@allure.title("Успешная регистрация пользователя")
def test_successful_registration_and_logout(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Заполнить поля валидными значениями и нажать на кнопку регичтрации
    3. Произвести logout из кабинета
    4. Проверить что пользователь вышел
    """
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).successful_registration()
    AccountPage(browser).check_registration_success()
    AccountPage(browser).logout()
    LoginPage(browser).check_logout_text()


@allure.feature("Регистрация пользователя")
@allure.title("Проверка регистрации при незаполненных полях")
def test_registration_error(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Не заполняя полей нажать на кнопку регистрация
    3. Проверить отображение алерта
    4. Проверить что под каждым полем отображается предупреждение"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 5


@allure.feature("Регистрация пользователя")
@allure.title("Проверка регистрации при заполнении одного обязательного поля First Name")
def test_registration_not_all_fields_1(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Заполнить поле First Name
    3. Не заполняя остальные поля нажать на кнопку регистрация
    4. Проверить отображение алерта
    5. Проверить что под каждым полем отображается предупреждение"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 4


@allure.feature("Регистрация пользователя")
@allure.title("Проверка регистрации при заполнении только First Name, Last Name")
def test_registration_not_all_fields_2(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Заполнить поля First Name и Last Name
    3. Не заполняя остальные поля нажать на кнопку регистрация
    4. Проверить отображение алерта
    5. Проверить что под каждым полем отображается предупреждение"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 3


@allure.feature("Регистрация пользователя")
@allure.title("Проверка регистрации при заполнении только First Name, Last Name, E-Mail")
def test_registration_not_all_fields_3(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Заполнить поля First Name Last Name E-Mail
    3. Не заполняя остальные поля нажать на кнопку регистрация
    4. Проверить отображение алерта
    5. Проверить что под каждым полем отображается предупреждение"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).enter_email()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 2


@allure.feature("Регистрация пользователя")
@allure.title("Проверка регистрации при заполнении только First Name, Last Name, E-Mail, Phone")
def test_registration_not_all_fields_4(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Заполнить поля First Name Last Name E-Mail Phone
    3. Не заполняя остальные поля нажать на кнопку регистрация
    4. Проверить отображение алерта
    5. Проверить что под каждым полем отображается предупреждение"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).enter_email()
    RegistrationPage(browser).enter_phone()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()
    text_danger = RegistrationPage(browser).count_text_danger()
    assert len(text_danger) == 1


@allure.feature("Регистрация пользователя")
@allure.title("Проверка регистрации при заполнении всех полей кроме подтверждения пароля")
def test_registration_not_all_fields_5(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Заполнить все поля кроме подтверждения пароля нажать на кнопку регистрация
    3. Проверить отображение алерта
    4. Проверить что под каждым полем отображается предупреждение"""
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


@allure.feature("Регистрация пользователя")
@allure.title("Проверка регистрации не активируя чек-бокс согласия")
def test_registration_not_all_fields_6(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Заполнить все поля не активируя чек-бокс "I have read and ..." нажать на кнопку регистрация
    3. Проверить отображение алерта
    4. Проверить что под каждым полем отображается предупреждение"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).enter_first_name()
    RegistrationPage(browser).enter_last_name()
    RegistrationPage(browser).enter_email()
    RegistrationPage(browser).enter_phone()
    RegistrationPage(browser).enter_password()
    RegistrationPage(browser).enter_confirm_password()
    RegistrationPage(browser).click_registration_button()
    SuccessAlert(browser).check_alert()


@allure.feature("Регистрация пользователя")
@allure.title("Проверка переключения радио кнопок Subscribe")
def test_registration_toggle_radio_buttons(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Нажать на каждую радио кнопку"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).click_on_radio_button_1()
    RegistrationPage(browser).click_on_radio_button_2()


@allure.feature("Регистрация пользователя")
@allure.title("Проверка модального окна Privacy Policy")
def test_registration_modal_privacy_policy(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Нажать на Privacy Policy
    3. Проверить отображение алерта с текстом
    4. Закрыть алерт"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).click_on_privacy_policy()
    RegistrationPage(browser).check_text_privacy_policy()
    SuccessAlert(browser).close_alert()


@allure.feature("Регистрация пользователя")
@allure.title("Проверка перехода на страницу login page")
def test_registration_go_to_login_page(browser):
    """Шаги:
    1. Перейти на страницу регистрации
    2. Нажать на текст login page
    3. Проверить что пользователь на странице login page"""
    MainPage(browser).go_to_registration()
    RegistrationPage(browser).click_login_page_button()
    LoginPage(browser).check_returning_customer_text()
