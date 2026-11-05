from locators import (PUBLISH_AD_BUTTON, UNAUTHORIZED_MODAL_TITLE, LOGIN_REGISTER_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, LOGIN_SUBMIT_BUTTON, USER_AVATAR, 
                      AD_TITLE_INPUT, AD_DESCRIPTION_INPUT, AD_PRICE_INPUT, AD_CATEGORY_DROPDOWN_ARROW, AD_CATEGORY_OPTION_HOBBY, 
                      AD_CITY_DROPDOWN_ARROW, AD_CITY_OPTION_KAZAN, AD_CONDITION_NEW_RADIO, AD_SUBMIT_BUTTON, MY_CREATED_AD_TITLE)


class TestAdvertisementCreation:
    def test_advert_no_user_authorized(self, driver):
        driver.find_element(*PUBLISH_AD_BUTTON).click()
        modal_title = driver.find_element(*UNAUTHORIZED_MODAL_TITLE)
        assert modal_title.is_displayed()
    
    def test_advert_user_authorized(self, driver):
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys("smirnova_38@gmail.com")
        driver.find_element(*PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        driver.find_element(*USER_AVATAR)
        driver.find_element(*PUBLISH_AD_BUTTON).click()
        driver.find_element(*AD_TITLE_INPUT).send_keys("Игрушки для кота")
        driver.find_element(*AD_DESCRIPTION_INPUT).send_keys("Коту не понравились, новые.")
        driver.find_element(*AD_PRICE_INPUT).send_keys("300")
        driver.find_element(*AD_CATEGORY_DROPDOWN_ARROW).click()
        driver.find_element(*AD_CATEGORY_OPTION_HOBBY).click()
        driver.find_element(*AD_CITY_DROPDOWN_ARROW).click()
        driver.find_element(*AD_CITY_OPTION_KAZAN).click()
        driver.find_element(*AD_CONDITION_NEW_RADIO).click() 
        driver.find_element(*AD_SUBMIT_BUTTON).click()
        avatar = driver.find_element(*USER_AVATAR)
        driver.execute_script("arguments[0].click();", avatar)
        my_ad = driver.find_element(*MY_CREATED_AD_TITLE)
        assert my_ad.is_displayed()
