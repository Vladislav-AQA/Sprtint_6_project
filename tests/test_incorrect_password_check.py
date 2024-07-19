from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver
import data

class TestIncorrectPassword:

    def test_incorrect_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        WebDriverWait.(driver,3).until(expected_conditions.visibility_of_element_located(*TestLocators.PASSWORD_INPUT))

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(data.PASSWORD_LESS_SIX_NUM)
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()

        assert driver.find_element(*TestLocators.ERROR_PASSWORD).text == "Некорректный пароль"

