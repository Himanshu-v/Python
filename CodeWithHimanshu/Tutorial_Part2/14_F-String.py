import math
# There are different ways to format strings but F-string gives readability.

# 1
a = 'Himanshu'
b = 25
c = 'My name is %s, I am %s.' % (a, b)
print(c)


# 2
c = 'My name is {}, I am {}.'
print(c.format(a, b))

# 3 F-String, F - FAST
c = f'My name is {a}, I am {b} and I have the offer of {math.factorial(10)}'
print(c)
