from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestBunSection:

    def test_move_to_bun_section():
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(*TestLocators.BUNS_SECTION))
        driver.find_element(*TestLocators.BUNS).click()


        assert 'current' in TestLocators.BUNS_SECTION



        driver.quit()