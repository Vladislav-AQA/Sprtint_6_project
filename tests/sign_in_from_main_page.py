from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver

class TestSignFromMain:

    def test_sign_in_from_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(*TestLocators.SIGN_IN_AN_ACCOUNT_BUTTON))
        driver.find_element(*TestLocators.SIGN_IN_AN_ACCOUNT_BUTTON).click()

        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(*TestLocators.SIGN_IN_BUTTON))
        assert TestLocators.SIGN_IN_BUTTON in TestLocators.SIGN_IN_FORM


        driver.quit()