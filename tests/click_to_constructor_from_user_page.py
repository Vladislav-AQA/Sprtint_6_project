from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from conftest import driver


class TestConstructor:

    def test_click_on_constructor(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(TestLocators.DASHBOARD))
        driver.find_element(*TestLocators.DASHBOARD).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(*TestLocators.CONSTRUCTOR))
        driver.find_element(*TestLocators.CONSTRUCTOR).click()

        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(*TestLocators.TITLE_BUNS))
        assert 'Соберите бургер' in TestLocators.BUNS_SECTION

        driver.quit()