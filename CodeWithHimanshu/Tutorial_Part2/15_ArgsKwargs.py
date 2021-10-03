def argadapt(normal, *args, **kwargs):  # Now this function is eligible to take * & **.
    print(f'this is {normal}')  # Always follow the order normal, *, **
    print(type(args))
    for item in args:
        print(item)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'{key} is {value}')


# argadapt("normal")  # *args and **kwargs are optional unless you use them inside the method.

lst = ["Himanshu", "is", "hot"]
# argadapt("Normal Argument", *lst)  # use * before the sequence

diction = {'Himanshu': 'Hot'}
argadapt("normal arg", *lst, **diction)