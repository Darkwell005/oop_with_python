with open("city.txt", "r", encoding="UTF-8") as file:
    content = file.readlines()
print(f"Количество строк в файле: {len(content)}")
