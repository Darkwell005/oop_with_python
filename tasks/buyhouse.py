class Human:
    default_name = "Alex"
    default_age = 18

    def __init__(self, name: str = default_name, age: int = default_age):
        self.name = name
        self.age = age
        __money = 0
        __house = False

    def default_info(self):
        print(self.default_name, self.default_age)
