import random


def add(x, y):
    return x + y


print(add(10, 112))

#  Lambda
addition = lambda x, y: x + y  # lambda <Parameters>: <Operations>

print(addition(11, 12))

# USING MODULES

ls = ["r", "s", 33.4, 25]
choice = random.choice(ls)
print(choice)

print(random.randint(1, 20))  # Random n in 1-20
print(random.random())  # Random n in 0-1
