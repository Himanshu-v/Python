a = 1
b = 2
c = sum([a, b])
print(c)


def average():
    """This is a function to print the average of two numbers."""  # This is DOCSTRING
    ave = (a + b) / 2
    return ave    # No need to specify return type in method definition!
    pass  # Do nothing

av = average()
print(av)

print(average.__doc__)

