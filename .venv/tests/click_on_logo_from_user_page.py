from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class TestLogo:

    def click_on_logo(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(By.TAG_NAME, "header"))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(By.TAG_NAME, "header"))
        driver.find_element(By.XPATH, ".//header//div").click()

        driver.quit()