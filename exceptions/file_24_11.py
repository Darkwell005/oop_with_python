def example_one():
    try:
        1 / 0
    except ZeroDivisionError:
        print(0)
    else:
        print(1)
    finally:
        print("Завершение")


def example_two():
    try:
        db = "db"
    except Exception as err:
        print(err)
    else:
        print(1)
    finally:
        print("Закрываем соединение")


def example_three(value: str) -> int:
    try:
        num: int = int(value)
    except ValueError:
        print("Введите целое число")
        return -1
    else:
        return num * 10
    finally:
        print("***")


class UserNameError(Exception):
    pass


def example_four(name: str):
    for char in name:
        if not char.isalpha():
            raise UserNameError(
                "Имя должна состоять только из букв"
            )

    return name


if __name__ == "__main__":
    example_four(input())
    # result = example_three("1.5")
    # print(result)
