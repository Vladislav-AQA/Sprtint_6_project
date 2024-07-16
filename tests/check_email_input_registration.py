from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver

class TestSuccessReg:

    def test_success_reg_user(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys('vladislav_11_123@yandex.ru')

        actually_email = driver.find_element(*TestLocators.NAME_INPUT).get_property("value")
        expected_email = 'vladislav_11_123@yandex.ru'
        assert actually_email == expected_email, f'Ожидаемое значение поля "Имя": "{expected_email}", получено: "{actually_email}"'

        driver.quit()