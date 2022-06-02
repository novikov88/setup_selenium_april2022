from selenium.webdriver.common.by import By
from exception_handler import *
from faker import Faker

# создаем экземпляр класса Faker для генерации данных
fake = Faker()


# тест успешная регистрация и выход из ЛК
def test_successful_registration_and_logout(browser):
    """Тест проверяет успешную регистрацию пользователя"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys(fake.last_name())
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(fake.email())
    browser.find_element(By.CSS_SELECTOR, "#input-telephone").send_keys(fake.phone_number())
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys('123456')
    browser.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys('123456')
    browser.find_element(By.NAME, "agree").click()
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]")
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.LINK_TEXT, 'Logout').click()
    browser.find_element(By.XPATH, "//h1[contains(text(),'Account Logout')]").click()


def test_registration_error(browser):
    """Тест проверяет отображение текста предупреждения к обязательным полям при нажатии кнопки регистрации при
    незаполненных полях"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    text_danger = wait_elements(browser, (By.CSS_SELECTOR, ".text-danger"))
    assert len(text_danger) == 5


def test_registration_not_all_fields_1(browser):
    """Тест включает заполнение одного обязательного поля First Name и нажатие на кнопку регистрации.
    Осуществляется проверка текста предупреждения к остальным обязательным полям"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    text_danger = wait_elements(browser, (By.CSS_SELECTOR, ".text-danger"))
    assert len(text_danger) == 4


def test_registration_not_all_fields_2(browser):
    """Тест включает заполнение двух обязательных полей First Name, Last Name и нажатие на кнопку регистрации.
    Осуществляется проверка текста предупреждения к остальным обязательным полям"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys(fake.last_name())
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    text_danger = wait_elements(browser, (By.CSS_SELECTOR, ".text-danger"))
    assert len(text_danger) == 3


def test_registration_not_all_fields_3(browser):
    """Тест включает заполнение трех обязательных полей First Name, Last Name, E-Mail и нажатие на кнопку регистрации.
    Осуществляется проверка текста предупреждения к остальным обязательным полям"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys(fake.last_name())
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(fake.email())
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    text_danger = wait_elements(browser, (By.CSS_SELECTOR, ".text-danger"))
    assert len(text_danger) == 2


def test_registration_not_all_fields_4(browser):
    """Тест включает заполнение 4х обязательных полей First Name, Last Name, E-Mail, Telephone и нажатие на кнопку
    регистрации. Осуществляется проверка текста предупреждения к остальным обязательным полям"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys(fake.last_name())
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(fake.email())
    browser.find_element(By.CSS_SELECTOR, "#input-telephone").send_keys(fake.phone_number())
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    text_danger = wait_elements(browser, (By.CSS_SELECTOR, ".text-danger"))
    assert len(text_danger) == 1


def test_registration_not_all_fields_5(browser):
    """Тест включает заполнение 5-и обязательных полей First Name, Last Name, E-Mail, Telephone, Password без
    подтверждения пароля и нажатие на кнопку регистрации. Осуществляется проверка текста предупреждения к полю
    подтверждения пароля"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys(fake.last_name())
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(fake.email())
    browser.find_element(By.CSS_SELECTOR, "#input-telephone").send_keys(fake.phone_number())
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(fake.password())
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    text_danger = wait_elements(browser, (By.CSS_SELECTOR, ".text-danger"))
    assert len(text_danger) == 1


def test_registration_not_all_fields_6(browser):
    """Тест включает заполнение всех обязательных полей, но без активации чекбокса "I have read and agree to the
    Privacy Policy ". Осуществляется проверка текста предупреждения к чекбоксу"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys(fake.name())
    browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys(fake.last_name())
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(fake.email())
    browser.find_element(By.CSS_SELECTOR, "#input-telephone").send_keys(fake.phone_number())
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys('123456')
    browser.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys('123456')
    browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    browser.find_element(By.CSS_SELECTOR, ".alert-dismissible")
    wait_element(browser, (By.CSS_SELECTOR, ".fa-exclamation-circle"))


def test_registration_toggle_radio_buttons(browser):
    """Тест включает проверку переключения радио кнопок Subscribe"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.XPATH, "//label[contains(text(),'Subscribe')]/../div[1]/label[1]").click()
    browser.find_element(By.XPATH, "//label[contains(text(),'Subscribe')]/../div[1]/label[2]").click()


def test_registration_modal_privacy_policy(browser):
    """Тест включает проверку отображения модального окна Privacy Policy"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.LINK_TEXT, 'Privacy Policy').click()
    wait_element(browser, (By.XPATH, "//h4[contains(text(),'Privacy Policy')]"))
    browser.find_element(By.XPATH, "//button[contains(text(),'×')]").click()


def test_registration_go_to_login_page(browser):
    """Тест включает проверку перехода на страницу login page"""
    browser.find_element(By.LINK_TEXT, 'My Account').click()
    browser.find_element(By.XPATH, "// a[contains(text(), 'Register')]").click()
    browser.find_element(By.LINK_TEXT, 'login page').click()
    wait_element(browser, (By.XPATH, "//h2[contains(text(),'Returning Customer')]"))
