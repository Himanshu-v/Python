print("Enter the first number")
a = input()
print("Enter the first number")
b = input()

try:
    print("The product is", int(a) * int(b))
except Exception as e:
    print(e)


print("This gets printed even after exception at line 7")
