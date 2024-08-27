import string
from string import ascii_lowercase


class BaseInput:
    digit = string.digits
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digit

    @classmethod
    def check_name(cls, name: str) -> None:
        length = len(name)
        if not (3 <= length < 50 and name in cls.CHARS_CORRECT):
            raise ValueError("Некорректное поле name")

    def __init__(self, name: str, size: int = 10):
        self.name = name
        self.size = size


class TextInput(BaseInput):
    def get_html(self) -> str:
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(BaseInput):
    def get_html(self) -> str:
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn: "TextInput", psw: "PasswordInput"):
        self.login = lgn
        self.password = psw

    def render_template(self) -> str:
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
