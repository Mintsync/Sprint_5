import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://qa-desk.education-services.ru/')
    yield browser
    browser.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 5)
