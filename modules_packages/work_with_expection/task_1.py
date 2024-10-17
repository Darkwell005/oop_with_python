# INFO: Согласно условию задачи, Вам необходимо написать функцию.
# Приведу два возможных решения

def get_num_from_user() -> int:
    num: str = input("Введите число: ")

    start: int = 10
    end: int = 20
    if (not num.isdigit()) or (not (start <= int(num) <= end)):
        raise ValueError(
            "Ошибка! Вы ввели не число или число не находится в диапазоне!"
        )

    return int(num)


# Можно сделать код ещё читабельнее
def validate_num(num: str):
    start: int = 10
    end: int = 20
    if (not num.isdigit()) or (not (start <= int(num) <= end)):
        raise ValueError(
            "Ошибка! Вы ввели не число или число не находится в диапазоне!"
        )


def get_num_from_user_short() -> int:
    num: str = input("Введите число: ")
    validate_num(num)

    return int(num)


if __name__ == "__main__":
    while True:
        try:
            number: int = get_num_from_user()
        except ValueError as error_msg:
            print(error_msg)
        except Exception as error_msg:
            print(f"Неожиданная ошибка: {error_msg}")
        else:
            print(f"Работаем с числом {number}")
            break

# Ещё в задаче сказано "Максимальная длина кода тела функции 4 строки:"
# не обращайте на это внимание, пишите читаемый и чистый код, вместо короткого
