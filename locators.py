from selenium.webdriver.coomon.by import By
class TestLocators:
    DASHBOARD = By.XPATH, ".//p[text()='Личный Кабинет']"
    LOGO = By.XPATH, ".//header//div"
    CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"
    NAME_INPUT = By.XPATH, ".//label[text()='Имя']/parent::div/input"
    EMAIL_INPUT = By.XPATH, ".//label[text()='Email']/parent::div/input"
    PASSWORD_INPUT = By.XPATH, ".//label[text()='Пароль']/parent::div/input"
    BUNS = By.XPATH, ".//span[text()='Булки']"
    BUNS_SECTION = By.XPATH, ".//div/h2[text()='Булки']"
    SAUCES = By.XPATH, ".//span[text()='Соусы']"
    SAUCES_SECTION = By.XPATH, ".//div/h2[text()='Соусы']"
    STUFFING = By.XPATH, ".//span[text()='Начинки']"
    STUFFING_SECTION = By.XPATH, ".//div/h2[text()='Начинки']"
    REGISTRATION_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"
    SIGN_IN_FORM = By.CLASS_NAME, "Auth_login__3hAey"
    SIGN_IN_BUTTON = By.XPATH, ".//button[text()='Войти']"
    SIGN_IN_AN_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    SIGN_IN_REGISTER_FORM = By.XPATH, ".//a[text()='Войти']"
    RESET_PASSWORD_BUTTON = By.XPATH, ".//form//button[text()='Восстановить']"
    SIGN_OUT_BUTTON = By.XPATH, ".//button[text()='Выход']"
    ERROR_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']"
    TITLE_BUNS = By.XPATH, ".//h1[text()='Соберите бургер']"