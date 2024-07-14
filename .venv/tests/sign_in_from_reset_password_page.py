from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class TestSignFromResetPass:

    def sign_in_from_reset_apss_page(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

        driver.find_element(By.XPATH, ".//form//button[text()='Восстановить']").click()
        driver.find_element(By.XPATH,  ".//label[text()='Email']/parent::div/input").send_keys(new_email)
        driver.find_element(By.XPATH,  ".//label[text()='Пароль']/parent::div/input").send_keys(new_password)



        driver.quit()