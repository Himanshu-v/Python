class A:
    classvar1 = "class var of class A"

    def __init__(self):
        self.instancevar = "instance variable of A"
        self.classvar1 = 'instance var of class A'


class B(A):
    classvar1 = "class var of class B"
    def __init__(self):
        super().__init__()
        self.instancevar = "instance variable of B"
        self.classvar1 = 'instance var of class B'



b = B()
print(b.classvar1)
