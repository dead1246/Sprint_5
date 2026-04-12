from random import choices, randint
from string import ascii_letters, digits


COHORT_NUMBER = "123"
EMAIL_DOMAIN = "yandex.ru"
EMAIL_PREFIX = "test_testov"


def generate_email() -> str:
    """Генерирует уникальный email в формате для учебного проекта."""
    random_tail = randint(100, 999)
    return f"{EMAIL_PREFIX}_{COHORT_NUMBER}_{random_tail}@{EMAIL_DOMAIN}"


def generate_password(length: int = 8) -> str:
    """Генерирует пароль заданной длины."""
    alphabet = ascii_letters + digits
    return "".join(choices(alphabet, k=length))


def build_user() -> dict[str, str]:
    """Собирает данные пользователя для регистрации."""
    return {
        "name": "Test User",
        "email": generate_email(),
        "password": generate_password(),
    }
