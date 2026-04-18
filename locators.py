from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_TO_ACCOUNT_BUTTON = (
        By.XPATH,
        "//main//button[contains(@class,'button_button_type_primary')]",
    )
    # Ссылка "Личный кабинет" в шапке
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//header//a[@href='/account']")
    # Ссылка "Конструктор" в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "(//header//a[@href='/'])[1]")
    # Логотип Stellar Burgers в шапке
    STELLAR_BURGERS_LOGO = (By.XPATH, "//header//a[.//*[local-name()='svg']]")
    # Заголовок главной страницы
    MAIN_HEADING = (By.XPATH, "//main//h1")


class LoginPageLocators:
    # Заголовок страницы входа
    LOGIN_HEADING = (By.XPATH, "//main//h2")
    # Поле Email на странице входа
    EMAIL_INPUT = (By.XPATH, "(//form//input)[1]")
    # Поле Пароль на странице входа
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Кнопка "Войти" на странице входа
    LOGIN_BUTTON = (
        By.XPATH,
        "//form//button[contains(@class,'button_button_type_primary')]",
    )
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")


class RegisterPageLocators:
    # Заголовок страницы регистрации
    REGISTER_HEADING = (By.XPATH, "//main//h2")
    # Поле Имя на странице регистрации
    NAME_INPUT = (By.XPATH, "(//form//input)[1]")
    # Поле Email на странице регистрации
    EMAIL_INPUT = (By.XPATH, "(//form//input)[2]")
    # Поле Пароль на странице регистрации
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (
        By.XPATH,
        "//form//button[contains(@class,'button_button_type_primary')]",
    )
    # Текст ошибки некорректного пароля
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[contains(@class,'input__error')]")
    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")


class ForgotPasswordPageLocators:
    # Заголовок страницы восстановления пароля
    FORGOT_PASSWORD_HEADING = (By.XPATH, "//main//h2")
    # Ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")


class AccountPageLocators:
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (
        By.XPATH,
        "//main//button[text()='Выход']",
    )
    # Блок профиля пользователя в личном кабинете
    PROFILE_FORM = (By.XPATH, "//form")


class ConstructorPageLocators:
    # Вкладка "Булки"
    BUNS_TAB = (
        By.XPATH,
        "(//div[contains(@class,'tab_tab')])[1]",
    )
    # Вкладка "Соусы"
    SAUCES_TAB = (
        By.XPATH,
        "(//div[contains(@class,'tab_tab')])[2]",
    )
    # Вкладка "Начинки"
    FILLINGS_TAB = (
        By.XPATH,
        "(//div[contains(@class,'tab_tab')])[3]",
    )
    # Заголовок секции "Соусы"
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    # Заголовок секции "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    # Заголовок секции "Булки"
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
