from locators import (LOGIN_REGISTER_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON, LOGOUT_BUTTON, USER_NAME_TEXT, USER_AVATAR)


class TestUserLogout:
    def test_logout(self, driver):
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys("smirnova_38@gmail.com")
        driver.find_element(*PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        driver.find_element(*LOGOUT_BUTTON).click()
        login_btn = driver.find_element(*LOGIN_REGISTER_BUTTON)
        assert login_btn.text == "Вход и регистрация"
        user_name = driver.find_elements(*USER_NAME_TEXT)
        assert len(user_name) == 0
        avatars = driver.find_elements(*USER_AVATAR)
        assert len(avatars) == 0
