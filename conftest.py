import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: ru, en, de, etc.")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        browser = webdriver.Chrome(options=options, executable_path="./drivers/chromedriver.exe")
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp, executable_path="./drivers/geckodriver.exe")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.maximize_window()
    yield browser
    browser.quit()
