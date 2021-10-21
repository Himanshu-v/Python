def factorial_recursive_m2(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive_m2(n - 1)


#  MAP: Start

ls = [1, 2, 3, 4]
fact = list(map(factorial_recursive_m2, ls))
print(fact)
square = list(map(lambda x: x * x, ls))
print(square)


def qube(x):
    return x * x * x


def square(x):
    return x * x


func = [qube, square]
for i in range(5):
    val = list(map(lambda x: x(i), func))  # applying the function in list func on i.
    print(val)


# MAP: End.  FILTER Start.
def is_greater_than_6(n):
    return n > 6


gt_2_lst = list(filter(is_greater_than_6, ls))
print(gt_2_lst)


# FILTER End. REDUCE Start.
from functools import reduce
num = reduce(lambda x,y: x-y, ls)
print(num)