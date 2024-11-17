def read_from_text_file(file_name: str) -> None:
    with open(file=file_name, mode="r", encoding="UTF-8") as file:
        names = file.readlines()

        for index, name in enumerate(names, start=1):
            print(index, name.rstrip().capitalize())


def write_to_text_file(
        data: list[str],
        file_name: str = "new_file.txt"
) -> None:
    with open(file=file_name, mode="w", encoding="UTF-8") as file:
        # for item in data:
        #     file.write(item + "\n")

        file.writelines(
            f"{item}\n" for item in data
        )


write_to_text_file(
    ["banana", "apple", "pineapple", "kiwi"],
    file_name="fruits.txt"
)

write_to_text_file(
    [1, 2, 3, 4],
    file_name="nums.txt"
)
