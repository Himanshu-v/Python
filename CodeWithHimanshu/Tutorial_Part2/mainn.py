list1 = ["One", "Two", "Three", "Four"]


def enumlist(x):
    for index, item in enumerate(x):
        if index % 2 == 0:
            print(item)


print(f"The name is {__name__}")  # '__main__' when this file is run, 'mainn' when called from other file.
joint = " and ".join(list1)
if __name__ == '__main__':
    enumlist(list1)
    print(joint)
