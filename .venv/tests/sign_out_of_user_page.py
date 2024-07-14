from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver

class TestSignOut:

    def sign_out_from_user_page(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')

        driver.find_element(By.XPATH,  ".//label[text()='Email']/parent::div/input").send_keys('vladislav_11_123@yandex.ru')
        driver.find_element(By.XPATH,  ".//label[text()='Пароль']/parent::div/input").send_keys('123456')
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(By.TAG_NAME, "header"))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

        driver.quit()