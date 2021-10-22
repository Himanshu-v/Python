class Person:
    type = "Intelligent"

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printouts(self):
        print(f"The name is {self.name}, He earns {self.salary} Crores per annum working as a {self.role} of HIS Firm.")

    # CLASS METHODS
    @classmethod
    def change_class_var(cls, newtype):
        cls.type = newtype

    @classmethod
    def alternative_constructor(cls, packd_args):
        return cls(*packd_args.split('-'))  #using args to pass multiple arguments in one go.


himanshu = Person("Himanshu Vishwakarma", 45, "Lead Software Engineer")
himanshu.printouts()  # py passes the calling instance to the method by default.
print(Person.type)
himanshu.type = "Awesome"
print("#Not changed#", Person.type)
himanshu.change_class_var("Awesome")  # Changes the class variable
print("Changed by instance to:", Person.type)
Person.change_class_var("Great")
print("Changed by class to:", Person.type)

# HOW classmethods CAN BE USED AS ALTERNATIVE CONSTRUCTOR TO CREATE AN OBJECT
himanshu = himanshu.alternative_constructor("THE HIMANSHU VISHWAKARMA-95-FOUNDER")  # can be called by class itself too
himanshu.printouts()
print(himanshu.__dict__)

