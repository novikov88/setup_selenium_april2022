import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=('chrome', 'firefox', 'edge', 'opera',
                                                                             'yandex'))
    parser.addoption("--url", action="store", default="http://192.168.1.67:8081/")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)

    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)

    elif browser == "opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())

    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path=f"{drivers}/yandexdriver")

    else:
        raise ValueError('Browser not supported')

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
