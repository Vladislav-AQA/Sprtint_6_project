from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class TestSignFromReg:

    def sign_in_from_reg_page(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        driver.find_element(By.XPATH,  ".//label[text()='Email']/parent::div/input").send_keys(new_email)
        driver.find_element(By.XPATH,  ".//label[text()='Пароль']/parent::div/input").send_keys(new_password)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()


        driver.quit()