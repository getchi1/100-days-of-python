#randomly getting heads or tails
import random

# random_number_int = random. randint(1, 100)
# print(random_number_int)

# random_float_0_to_1 = random.random() * 12
# print(random_float_0_to_1)

# random_float = random.uniform(0, 100)
# print(random_float)

coin = random.randint(0,1)
print(coin)
if coin == 0:
    print("Heads")
else:
    print("Tails")