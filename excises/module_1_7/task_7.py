import string


class Data:
    digit = "0123456789"
    ascii_lowercase = string.ascii_lowercase
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digit

    @classmethod
    def check_name(cls, name: str):
        if (3 <= len(name) < 50) and name in cls.CHARS_CORRECT:
            pass
        else:
            raise ValueError("Некорректное поле name")

    def __init__(self, name: str, size=10):
        self.name = name
        self.size = size

    def get_html(self):
        if TextInput:
            return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
        elif PasswordInput:
            return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class TextInput(Data):
    pass


class PasswordInput(Data):
    pass


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
