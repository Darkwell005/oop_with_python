with open("city.txt", "r", encoding="UTF-8") as reader:
    with open("city_2.txt", "w", encoding="UTF-8") as writer:
        for x in reader:
            if "о" not in x.strip("\n"):
                writer.writelines(x)
                