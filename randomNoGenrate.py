#python program to generate a random number and string

import random
import string
num = random.randint(1,6)
p=(''.join(random.choices(string.ascii_letters, k=5)))
print(p)
print(num)

