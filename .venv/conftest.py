import pytest
import random
from random import choice

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def new_name(driver):
    name = ['Vladimir', 'Vasily', 'Anastasia', 'Andrey', 'Zahar', 'Svetlana']
    new_name = random.choice(name)
    return new_name(driver)

@pytest.fixture
def new_email(driver):
    new_email = f"{random.randint(100.999)}@ya.ru"
    return new_email(driver)

@pytest.fixture
def new_password(driver):
    new_password = random.randint(111111,999999)
    return new_password(driver)

@pytest.fixture
def new_incorrect_password(driver):
    new_incorrect_password = random.randint(111,456)
    return new_incorrect_password(driver)