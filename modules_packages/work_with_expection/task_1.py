for _ in range(4):
    try:
        user_input = int(input())
        if 10 < user_input <= 20:
            print(f"Работаем с числом {user_input}")


    except ValueError:
        print("Ошибка! Вы ввели не число или число не находится в диапазоне!")
