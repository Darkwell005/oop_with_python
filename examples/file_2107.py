# # Класс - описание сущности
#
#
# # Чертеж
# class Animal:
#     COLOR: str = ''
#
#
#     def zvuk(self):
#         pass
#
#
# # Объект | Экземпляр
#
#
# kot_boris = Animal()
# dog_chack = Animal()
#
#
# class House:
#     pass
#
#
# large_red_house = House()

# ----------------------------------


# class Car:
#     WHEEL: int = 4  # Свойство | Поле | Атрибут класса
#
#     # Метод класса (Поведение)
#     def rul(self):
#         print('Руль')
#
#     def signal(self):
#         print('Сигнал')
#
#
# # Объект | Экземпляр
# red_car: Car = Car()
# red_car.signal()
# yellow_car = Car()
# yellow_car.signal()
#
# print(red_car.WHEEL)
#
#
# line: str = 'Hello, World!'
# line_2: str = 'Привет, Мир!'
# line.isalpha()
#
#
# result: list[int] = list()
#
# result.count(10)


# ----------------------------------

class Human:
    # Конструктор класса
    def __init__(self,
                 name: str,
                 date_of_birth: str,
                 height: int | float) -> None:
        # Динамические свойства | поля | атрибуты
        self.name = name
        self.date_of_birth = date_of_birth
        self.height = height

    def info(self):
        print(
            f'\nИмя: {self.name}'
            f'\nДата рождения: {self.date_of_birth}'
            f'\nРост: {self.height}'
        )

    def get_age(self, current_year: str) -> int:
        day, month, year = self.date_of_birth.split('.')
        age: int = int(current_year) - int(year)
        return age


vasya = Human('Вася', '01.01.1970', 175)
# print(vasya.name, vasya.date_of_birth, vasya.height)

petya = Human('Петя', '02.02.1990', 180)
# print(petya.name, petya.date_of_birth, petya.height)


vasya.info()
petya.info()

print(f'Возраст {vasya.name}: {vasya.get_age("2024")}')
print(f'Возраст {petya.name}: {petya.get_age("2024")}')
