from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver

class TestSuccessReg:

    def test_success_reg_user(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.NAME_INPUT).send_keys('Vladislav')

        actually_name = driver.find_element(*TestLocators.NAME_INPUT).get_property("value")
        expected_name = 'Vladislav'
        assert actually_name == expected_name, f'Ожидаемое значение поля "Имя": "{expected_name}", получено: "{actually_name}"'

        driver.quit()