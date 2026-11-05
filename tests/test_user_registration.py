import random
import string
from selenium.webdriver.support import expected_conditions as EC
from locators import (LOGIN_REGISTER_BUTTON, NO_ACCOUNT_LINK, EMAIL_INPUT, PASSWORD_INPUT, PASSWORD_CONFIRM_INPUT, REGISTER_SUBMIT_BUTTON, 
                      USER_NAME_TEXT, USER_AVATAR, FORM_ERROR_MESSAGE, INVALID_EMAIL_CONTAINER, INVALID_PASSWORD_CONTAINER, INVALID_CONFIRM_PASSWORD_CONTAINER)


class TestRegistration:
    def test_register_new_user(self, driver, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_LINK)).click()
        random_letters = [random.choice(string.ascii_lowercase) for _ in range(7)]
        testing_email = "".join(random_letters) + '@gmail.com'
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(testing_email)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("12345")
        wait.until(EC.visibility_of_element_located(PASSWORD_CONFIRM_INPUT)).send_keys("12345")
        wait.until(EC.element_to_be_clickable(REGISTER_SUBMIT_BUTTON)).click()
        wait.until(EC.url_to_be('https://qa-desk.education-services.ru/regiatration'))
        user_name = wait.until(EC.visibility_of_element_located(USER_NAME_TEXT))
        assert user_name.text == "User."
        avatar = wait.until(EC.visibility_of_element_located(USER_AVATAR))
        assert avatar.is_displayed()

    def test_register_invalid_email(self, driver, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_LINK)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys("sm_38gmailcom")
        wait.until(EC.element_to_be_clickable(REGISTER_SUBMIT_BUTTON)).click()
        error = wait.until(EC.visibility_of_element_located(FORM_ERROR_MESSAGE))
        assert error.is_displayed()
        assert wait.until(EC.visibility_of_element_located(INVALID_EMAIL_CONTAINER)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(INVALID_PASSWORD_CONTAINER)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(INVALID_CONFIRM_PASSWORD_CONTAINER)).is_displayed()

    def test_register_existing_user(self, driver, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_LINK)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys("smirnova_38@gmail.com")
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("12345")
        wait.until(EC.visibility_of_element_located(PASSWORD_CONFIRM_INPUT)).send_keys("12345")
        wait.until(EC.element_to_be_clickable(REGISTER_SUBMIT_BUTTON)).click()
        error = wait.until(EC.visibility_of_element_located(FORM_ERROR_MESSAGE))
        assert error.is_displayed()
        assert wait.until(EC.visibility_of_element_located(INVALID_EMAIL_CONTAINER)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(INVALID_PASSWORD_CONTAINER)).is_displayed()
        assert wait.until(EC.visibility_of_element_located(INVALID_CONFIRM_PASSWORD_CONTAINER)).is_displayed()
