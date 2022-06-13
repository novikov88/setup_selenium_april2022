import json

import pytest
import os
import logging
import datetime
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from webdriver_manager.opera import OperaDriverManager


# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", choices=('chrome', 'firefox', 'edge', 'opera',
#                                                                              'yandex'))
#     parser.addoption("--url", action="store", default="http://192.168.1.67:8081/")
#     parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))
#     parser.addoption("--log_level", action="store", default="DEBUG")
#
#
# @pytest.fixture
# def browser(request):
#     # Сбор параметров запуска для pytest
#     browser = request.config.getoption("--browser")
#     url = request.config.getoption("--url")
#     drivers = request.config.getoption("--drivers")
#     log_level = request.config.getoption("--log_level")
#
#     logger = logging.getLogger(request.node.name)
#     file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
#     file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
#     logger.addHandler(file_handler)
#     logger.setLevel(level=log_level)
#
#     logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))
#
#     if browser == "chrome":
#         service = ChromiumService(executable_path=drivers + "/chromedriver")
#         driver = webdriver.Chrome(service=service)
#
#     elif browser == "firefox":
#         service = FFService(executable_path=drivers + "/geckodriver")
#         driver = webdriver.Firefox(service=service)
#
#     elif browser == "opera":
#         driver = webdriver.Opera(executable_path=OperaDriverManager().install())
#
#     elif browser == "yandex":
#         driver = webdriver.Chrome(executable_path=f"{drivers}/yandexdriver")
#
#     else:
#         raise ValueError('Browser not supported')
#
#     driver.log_level = log_level
#     driver.logger = logger
#     driver.test_name = request.node.name
#
#     logger.info("Browser:{}".format(browser, driver.desired_capabilities))
#
#     driver.maximize_window()
#
#     def fin():
#         driver.quit()
#         logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))
#
#     request.addfinalizer(fin)
#
#     driver.get(url)
#     driver.url = url
#
#     return driver
# DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=('chrome', 'firefox', 'edge', 'opera',
                                                                             'yandex'))
    parser.addoption("--url", action="store", default="http://192.168.1.67:8081/")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    drivers = request.config.getoption("--drivers")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

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
        driver = webdriver.Remote(
            command_executor="http://{}:4444/wd/hub".format(url),
            desired_capabilities={"browserName": browser}
        )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    driver.maximize_window()

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON
    )

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    driver.get(url)
    driver.url = url
    return driver
