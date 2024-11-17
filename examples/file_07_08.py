import sys

from oop_principes import Hou

# Потоковый ввод/вывод.
#           stdin/stdout

# data = input()
# print(data)

# -----------

# data: str = sys.stdin.read()
# data: str = sys.stdin.readline()
data: list = sys.stdin.readlines()
# print(data)

sys.stdout.write("".join(data))
