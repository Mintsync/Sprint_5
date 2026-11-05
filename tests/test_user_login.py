from selenium.webdriver.support import expected_conditions as EC
from locators import (LOGIN_REGISTER_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON, USER_NAME_TEXT, USER_AVATAR)


class TestUserLogin:
    def test_login(self, driver, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys("smirnova_38@gmail.com")
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("12345")
        wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)).click()
        assert driver.current_url == 'https://qa-desk.education-services.ru/login'
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME_TEXT))
        assert user_name.text == "User."
        avatar = wait.until(EC.visibility_of_element_located(USER_AVATAR))
        assert avatar.is_displayed()
