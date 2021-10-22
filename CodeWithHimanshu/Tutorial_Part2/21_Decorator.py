def func1():
    print("func1")


def func2(func):
    def func3():
        print(f"Executing {func.__name__}")
        func()
        print(f"Executed {func.__name__}")

    return func3

@func2
def func4():
    print("func4")


#func4 = func2(func4)   -- This line can be replaced by @func2 on func4 definition.
func4()


