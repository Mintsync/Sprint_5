from locators import (LOGIN_REGISTER_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON, USER_NAME_TEXT, USER_AVATAR)


class TestUserLogin:
    def test_login(self, driver):
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys("smirnova_38@gmail.com")
        driver.find_element(*PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        assert driver.current_url == 'https://qa-desk.education-services.ru/login'
        user_name = driver.find_element(*USER_NAME_TEXT)
        assert user_name.text == "User."
        avatar = driver.find_element(*USER_AVATAR)
        assert avatar.is_displayed()
