from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver

class TestSuccessReg:

    def test_success_reg_user(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.NAME_INPUT).send_keys('Valentina')
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys('valentina_73_773@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(*TestLocators.SIGN_IN_BUTTON))

        assert driver.find_element(*TestLocators.SIGN_IN_BUTTON).text == "Войти"

