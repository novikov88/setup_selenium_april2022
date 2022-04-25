from selenium import webdriver

DRIVERS = "/home/vladimir/Downloads/drivers"


def test_first():
    browser = webdriver.Chrome(executable_path=DRIVERS + "/chromedriver")
    browser.get('http://192.168.1.65:8081/')
    assert "Your Store" == browser.title
