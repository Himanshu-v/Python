class Student:
    school_name = "DCS"  # class variable. Shared by all instance.
    pass


him = Student()
her = Student()

him.name = "Himanshu"
him.subjects= ["A", "B", "C"]
her.name = "Himanshii"
him.school_name = "PPP"  # Changes the value for the instance. Instance variable
print(him.school_name)
print(Student.school_name)
Student.school_name="CHG"  # changed the class variable
print(Student.school_name)


print(her.__dict__, him.__dict__)