with open("numbers.txt", "w") as file:
    for i in range(1, 10001):
        file.write(str(i) + "\n")
