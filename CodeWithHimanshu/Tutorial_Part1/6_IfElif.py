"""
print("Enter your age")
age = int(input())

if age > 18:
    print("You can drive")
elif age == 18:
    print("Visit the office")
else:
    print("Bade hojao bete, kya jaldi hai?")
"""
# FAULTY CALCULATOR
"""
print("Choose one of the operations [*, /, +]")
operator = input()
print("Enter the first number")
num1 = input()
print("Enter the second number")
num2 = input()

if operator == '+':
    if num1 == '56' and num2 == '9':
        print(77)
    else:
        print(int(num1) + int(num2))

if operator == '*':
    if num1 == '45' and num2 == '3':
        print(555)
    else:
        print(int(num1) * int(num2))

if operator == '/':
    if num1 == '56' and num2 == '6':
        print(4)
    else:
        print(int(num1) / int(num2))
"""

# SHORT HAND IF ELSE
a = 2
b = 4
if a < b: print(True)

print(True) if a < b else print(False)
