with open("surnames.txt", "r", encoding="UTF-8") as reader:
    with open("woman.txt", "w", encoding="UTF-8") as woman:
        with open("man.txt", "w", encoding="UTF-8") as man:
            for x in reader:
                if (x.strip("\n").endswith("ВА")
                        or x.strip("\n").endswith("НА")
                        or x.strip("\n").endswith("АЯ")):
                    woman.writelines(x)
                else:
                    man.writelines(x)
