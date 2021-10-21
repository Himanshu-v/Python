sameNameVar = 22

print(sameNameVar)


def getvar():
    # sameNameVar=45  we cannot assign the value in the same scope before global dec.
    #    print(sameNameVar)  If we try to use the variable before global dec. It gives an error.
    global sameNameVar
    sameNameVar = 33
    print(sameNameVar)


getvar()
print(sameNameVar)  # Value of the global variable is changed by getVar()


def nestedfunction():
    sameNameVar1 = 34

    def nestedfunc2():
        global sameNameVar1
        sameNameVar1 = 44

    print("before", sameNameVar1)
    nestedfunc2()
    print("after", sameNameVar1)
    """Even if the sameNameVar1 is made global it wont affect the value in local scope of parent function. Because 
    global keyword only looks for the varable in global scope. If it does not find any, it creates one with the same
    name used after the keyword. If that variable is printed in the global scope it holds the same value defined."""


nestedfunction()
print(sameNameVar1)  # Prints the value defined in nestedFunc2 with the 'global' keyword.
