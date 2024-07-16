from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

from conftest import driver

class TestStuffingSection:

    def test_move_to_stuffing_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(*TestLocators.STUFFING_SECTION))

        driver.find_element(*TestLocators.STUFFING).click()

        assert 'current' in TestLocators.SELECT_STUFFING

        driver.quit()