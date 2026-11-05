from selenium.webdriver.support import expected_conditions as EC
from locators import (PUBLISH_AD_BUTTON, UNAUTHORIZED_MODAL_TITLE, LOGIN_REGISTER_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON, USER_AVATAR, 
                      AD_TITLE_INPUT, AD_DESCRIPTION_INPUT, AD_PRICE_INPUT, AD_CATEGORY_DROPDOWN_ARROW, AD_CATEGORY_OPTION_HOBBY, 
                      AD_CITY_DROPDOWN_ARROW, AD_CITY_OPTION_KAZAN, AD_CONDITION_NEW_RADIO, AD_SUBMIT_BUTTON, MY_CREATED_AD_TITLE)


class TestAdvertisementCreation:
    def test_advert_no_user_authorized(self, driver, wait):
        wait.until(EC.element_to_be_clickable(PUBLISH_AD_BUTTON)).click()
        modal_title = wait.until(EC.visibility_of_element_located(UNAUTHORIZED_MODAL_TITLE))
        assert modal_title.is_displayed()
    
    def test_advert_user_authorized(self, driver, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys("smirnova_38@gmail.com")
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("12345")
        wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(USER_AVATAR))
        wait.until(EC.element_to_be_clickable(PUBLISH_AD_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AD_TITLE_INPUT)).send_keys("Игрушки для кота")
        wait.until(EC.visibility_of_element_located(AD_DESCRIPTION_INPUT)).send_keys("Коту не понравились, новые.")
        wait.until(EC.visibility_of_element_located(AD_PRICE_INPUT)).send_keys("300")
        wait.until(EC.element_to_be_clickable(AD_CATEGORY_DROPDOWN_ARROW)).click()
        wait.until(EC.element_to_be_clickable(AD_CATEGORY_OPTION_HOBBY)).click()
        wait.until(EC.element_to_be_clickable(AD_CITY_DROPDOWN_ARROW)).click()
        wait.until(EC.element_to_be_clickable(AD_CITY_OPTION_KAZAN)).click()
        wait.until(EC.element_to_be_clickable(AD_CONDITION_NEW_RADIO)).click() 
        wait.until(EC.element_to_be_clickable(AD_SUBMIT_BUTTON)).click()
        avatar = wait.until(EC.presence_of_element_located(USER_AVATAR))
        driver.execute_script("arguments[0].click();", avatar)
        my_ad = wait.until(EC.visibility_of_element_located(MY_CREATED_AD_TITLE))
        assert my_ad.is_displayed()
