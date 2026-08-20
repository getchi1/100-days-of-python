import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#first way
# random_friends = random.choice(friends)
# print(random_friends)

#second way
random_friends = random.randint(0, 4)
print(random_friends)
print(friends[random_friends])



