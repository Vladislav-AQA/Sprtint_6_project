from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver

class TestSuccessReg:

    def test_success_reg_user(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('123456')

        actually_password = driver.find_element(*TestLocators.NAME_INPUT).get_property("value")
        expected_password = '123456'
        assert actually_password == expected_password, f'Ожидаемое значение поля "Имя": "{expected_password}", получено: "{actually_password}"'

        driver.quit()