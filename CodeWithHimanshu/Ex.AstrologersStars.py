print("Please enter the number of rows")
r = int(input())
print("Is pattern unreversed?")
isUnRev = int(input("1 for True, 0 for False\n"))

if isUnRev == 1:
    for i in range(0, r):
        for j in range(0, i+1):
            print('*', end=" ")
        print()
else:
    for i in range(r+1, 0, -1):
        for j in range(0, i-1):
            print('*', end=" ")
        print()



