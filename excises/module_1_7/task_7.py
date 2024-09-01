import string


class BaseInput:
    __digit: str = string.digits
    __cyrillic: str = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
    __CHARS: str = __cyrillic + string.ascii_lowercase
    __CHARS_CORRECT: str = __CHARS + __CHARS.upper() + __digit

    def __init__(self, name: str, size: int = 10):
        self.name = name
        self.size = size

    @classmethod
    def check_name(cls, name: str) -> None:
        length = len(name)
        name_min_length: int = 3
        name_max_length: int = 50
        if not (name_min_length <= length < name_max_length
                and name in cls.__CHARS_CORRECT):
            raise ValueError("Некорректное поле name")


class TextInput(BaseInput):

    def get_html(self) -> str:
        return (f"<p class='login'>{self.name}: "
                f"<input type='text' size={self.size} />")


class PasswordInput(BaseInput):
    def get_html(self) -> str:
        return (f"<p class='password'>{self.name}: "
                f"<input type='text' size={self.size} />")


class FormLogin:
    def __init__(self, lgn: "TextInput", psw: "PasswordInput"):
        self.login = lgn
        self.password = psw

    def render_template(self) -> str:
        return ("\n".join(['<form action="#">',
                           self.login.get_html(),
                           self.password.get_html(), '</form>']))


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
