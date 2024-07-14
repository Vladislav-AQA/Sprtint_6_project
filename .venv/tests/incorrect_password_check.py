from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class TestIncorrectPassword:

    def incorrect_password(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH,  ".//label[text()='Имя']/parent::div/input").send_keys(new_name)
        dirver.find_element(By.XPATH,  ".//label[text()='Email']/parent::div/input").send_keys(new_email)
        driver.find_element(By.XPATH,  ".//label[text()='Пароль']/parent::div/input").send_keys(new_incorrect_password)

        driver.quit()