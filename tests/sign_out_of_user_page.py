from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver

class TestSignOut:

    def test_sign_out_from_user_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys('vladislav_11_123@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(*TestLocators.LOGO))
        driver.find_element(*TestLocators.DASHBOARD).click()

        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(*TestLocators.SIGN_OUT_BUTTON))
        driver.find_element(*TestLocators.SIGN_OUT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(*TestLocators.SIGN_IN_BUTTON))
        assert TestLocators.SIGN_IN_BUTTON in TestLocators.SIGN_IN_FORM

        driver.quit()