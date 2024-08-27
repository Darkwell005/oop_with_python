from string import ascii_lowercase


class BaseInput:
    digit = "0123456789"  # TODO: 1. Используйте digits из string
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digit

    @classmethod
    def check_name(cls, name: str):
        # TODO: 2. Можно улучшить
        if (3 <= len(name) < 50) and name in cls.CHARS_CORRECT:
            pass
        else:
            raise ValueError("Некорректное поле name")

    def __init__(self, name: str, size: int = 10):
        self.name = name
        self.size = size

    def get_html(self):
        # TODO: 3. Как работают эти проверки?
        #  Может в каждом дочерним классе реализовать этот метод?
        if TextInput:
            return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
        elif PasswordInput:
            return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class TextInput(BaseInput):
    pass


class PasswordInput(BaseInput):
    pass


class FormLogin:
    # TODO: 4. Нужны аннотации
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
