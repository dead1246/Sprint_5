from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Ссылка "Личный кабинет" в шапке
    PERSONAL_ACCOUNT_LINK = (By.LINK_TEXT, "Личный Кабинет")
    # Ссылка "Конструктор" в шапке
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
    # Логотип Stellar Burgers в шапке
    STELLAR_BURGERS_LOGO = (By.XPATH, "//header//a[@href='/']")
    # Заголовок главной страницы
    MAIN_HEADING = (By.XPATH, "//h1[text()='Соберите бургер']")


class LoginPageLocators:
    # Заголовок страницы входа
    LOGIN_HEADING = (By.XPATH, "//h2[text()='Вход']")
    # Поле Email на странице входа
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input | //input[@name='name']")
    # Поле Пароль на странице входа
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Кнопка "Войти" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")


class RegisterPageLocators:
    # Заголовок страницы регистрации
    REGISTER_HEADING = (By.XPATH, "//h2[text()='Регистрация']")
    # Поле Имя на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле Email на странице регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле Пароль на странице регистрации
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Текст ошибки некорректного пароля
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//*[text()='Некорректный пароль']")
    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK = (By.LINK_TEXT, "Войти")


class ForgotPasswordPageLocators:
    # Заголовок страницы восстановления пароля
    FORGOT_PASSWORD_HEADING = (By.XPATH, "//h2[text()='Восстановление пароля']")
    # Ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK = (By.LINK_TEXT, "Войти")


class AccountPageLocators:
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # Блок профиля пользователя в личном кабинете
    PROFILE_FORM = (By.XPATH, "//form")


class ConstructorPageLocators:
    # Вкладка "Булки"
    BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab')][.//span[text()='Булки']]",
    )
    # Вкладка "Соусы"
    SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab')][.//span[text()='Соусы']]",
    )
    # Вкладка "Начинки"
    FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab')][.//span[text()='Начинки']]",
    )
    # Активная вкладка "Булки"
    ACTIVE_BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')][.//span[text()='Булки']]",
    )
    # Активная вкладка "Соусы"
    ACTIVE_SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')][.//span[text()='Соусы']]",
    )
    # Активная вкладка "Начинки"
    ACTIVE_FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class,'tab_tab_type_current')][.//span[text()='Начинки']]",
    )
    # Заголовок секции "Соусы"
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    # Заголовок секции "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    # Заголовок секции "Булки"
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
