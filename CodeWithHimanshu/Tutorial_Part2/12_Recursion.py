#  Calling a function inside a function is Recursion in programming

def factorial_iterative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


# print('The factorial of n is:', factorial_iterative(int(input("Enter the number to calculate the factorial"))))


def factorial_recursive(n):
    if n > 0:
        return n * factorial_iterative(n - 1)


# print('The rec_factorial of n is:', factorial_recursive(int(input("Enter the number to calculate the factorial"))))


def factorial_recursive_m2(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive_m2(n-1)



#print('The rec_factorial_m2 of n is:', factorial_recursive_m2(int(input("Enter the number to calculate the factorial\n"))))
ls = [1,2,3,4,5]
fact = list(map(factorial_recursive_m2, ls))
print(fact)

"""
HOW RECURSIVE FACT WORKS

5 * fact(4)
5 * 4 * fact(3)
5 * 4 * 3 * fact(2)
5 * 4 * 3 * 2 * fact(1)
5 * 4 * 3 * 2 * 1 = 123

"""