from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver

class TestIncorrectPassword:

    def test_incorrect_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('12345')

        error = driver.find_element(*TestLocators.ERROR_PASSWORD).text
        assert 'Некорректный пароль' in error

        driver.quit()