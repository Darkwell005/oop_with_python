import random
import string

lst = string.ascii_lowercase + string.ascii_uppercase
print(random.choices(lst, k=10))
