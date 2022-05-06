def test_first(browser):
    assert "Your Store" == browser.title
    browser.save_screenshot("test.png")
