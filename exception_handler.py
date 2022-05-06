from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element(driver, locator, timeout=1):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        driver.save_screenshot("test.png")
        raise AssertionError(f"Не дождался элемент {locator}")


# def wait_dropdown_currency(driver, locator, timeout=0):
#     try:
#         return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
#     except TimeoutException:
#         driver.save_screenshot("test.png")
#         raise AssertionError(f"Не дождался элемент {locator}")
