import random
import string
from selenium.common.exceptions import StaleElementReferenceException
from locators import (LOGIN_REGISTER_BUTTON, NO_ACCOUNT_LINK, EMAIL_INPUT, PASSWORD_INPUT, PASSWORD_CONFIRM_INPUT, REGISTER_SUBMIT_BUTTON, 
                      USER_NAME_TEXT, USER_AVATAR, FORM_ERROR_MESSAGE, INVALID_EMAIL_CONTAINER, INVALID_PASSWORD_CONTAINER, INVALID_CONFIRM_PASSWORD_CONTAINER)


class TestRegistration:
    def test_register_new_user(self, driver):
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_LINK).click()
        random_letters = [random.choice(string.ascii_lowercase) for _ in range(7)]
        testing_email = "".join(random_letters) + '@gmail.com'
        driver.find_element(*EMAIL_INPUT).send_keys(testing_email)
        driver.find_element(*PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*PASSWORD_CONFIRM_INPUT).send_keys("12345")
        driver.find_element(*REGISTER_SUBMIT_BUTTON).click()
        assert driver.current_url == 'https://qa-desk.education-services.ru/regiatration'
        user_name = driver.find_element(*USER_NAME_TEXT)
        assert user_name.text == "User."
        avatar = driver.find_element(*USER_AVATAR)
        assert avatar.is_displayed()

    def test_register_invalid_email(self, driver):
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_LINK).click()
        try:
            driver.find_element(*EMAIL_INPUT).send_keys("sm_38gmailcom")
        except StaleElementReferenceException:
            driver.find_element(*EMAIL_INPUT).send_keys("sm_38gmailcom")
        driver.find_element(*REGISTER_SUBMIT_BUTTON).click()
        error = driver.find_element(*FORM_ERROR_MESSAGE)
        assert error.is_displayed()
        email_error = driver.find_element(*INVALID_EMAIL_CONTAINER)
        password_error = driver.find_element(*INVALID_PASSWORD_CONTAINER)
        confirm_password_error = driver.find_element(*INVALID_CONFIRM_PASSWORD_CONTAINER)
        assert email_error.is_displayed()
        assert password_error.is_displayed()
        assert confirm_password_error.is_displayed()

    def test_register_existing_user(self, driver):
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_LINK).click()
        driver.find_element(*EMAIL_INPUT).send_keys("smirnova_38@gmail.com")
        driver.find_element(*PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*PASSWORD_CONFIRM_INPUT).send_keys("12345")
        driver.find_element(*REGISTER_SUBMIT_BUTTON).click()
        error = driver.find_element(*FORM_ERROR_MESSAGE)
        assert error.is_displayed()
        email_error = driver.find_element(*INVALID_EMAIL_CONTAINER)
        password_error = driver.find_element(*INVALID_PASSWORD_CONTAINER)
        confirm_password_error = driver.find_element(*INVALID_CONFIRM_PASSWORD_CONTAINER)
        assert email_error.is_displayed()
        assert password_error.is_displayed()
        assert confirm_password_error.is_displayed()
