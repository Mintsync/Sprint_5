import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://qa-desk.education-services.ru/')
    yield browser
    browser.quit()
