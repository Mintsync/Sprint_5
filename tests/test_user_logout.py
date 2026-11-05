from selenium.webdriver.support import expected_conditions as EC
from locators import (LOGIN_REGISTER_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON, LOGOUT_BUTTON, USER_NAME_TEXT, USER_AVATAR)


class TestUserLogout:
    def test_logout(self, driver, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys("smirnova_38@gmail.com")
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("12345")
        wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        login_btn = wait.until(EC.visibility_of_element_located(LOGIN_REGISTER_BUTTON))
        assert login_btn.text == "Вход и регистрация"
        assert wait.until(EC.invisibility_of_element_located(USER_NAME_TEXT))
        assert wait.until(EC.invisibility_of_element_located(USER_AVATAR))
