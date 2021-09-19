listOfList = [[1, 'a'], ['name', 'himanshu'], ['age', 25]]

for item, val in listOfList:
    print(item, val)

# Converting listOfList to dictionary
dict1 = dict(listOfList)
print(dict1)

for item in dict1:
    print(item)

"""for item, val in dict: Error.
 #   print(item, val)
"""
for item, val in dict1.items():
    print(item, val)

# QUIZ
list1 = ["name", 25, 'A', 5, 10]
for item in list1:
    if str(item).isnumeric() and item < 20:  # Typecast item into string so that isnumeric() function can be used.
        print(item)


# WHILE LOOP
print("While Loop")
i = 1
while i < 5:
    print(i)
    i = i+1

