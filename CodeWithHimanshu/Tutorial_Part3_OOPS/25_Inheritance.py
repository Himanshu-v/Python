class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"Name is {self.name} and age is {self.age}")


class Sportsman:
    games = ["Badminton", "Basketball", "Rifle Shooting"]

    def __init__(self, name, age, games):
        self.name = name
        self.age = age
        self.games = games

    def print_sp_details(self):
        print(f"Name is {self.name} and age is {self.age} and he plays {self.games}")

# SINGLE INHERITANCE


class Person(Employee):
    pass


histi = Person("Histi", 25)
histi.print_details()


class Person2(Sportsman):
    pass


misti = Person2("Misti", 23, ["Badminton"])
misti.print_sp_details()


# MULTIPLE INHERITANCE

class Person3(Employee, Sportsman):  # the order of specifying parent class is important.
    pass


timmi = Person3("Timmi", 22)
timmi.games = ["carrom"]
timmi.print_sp_details()  # From Sportsman
timmi.print_details()  # From Employee


# MULTI LEVEL INHERITANCE

class Player(Sportsman):
    plays = "Plays 5 times a week"
    pass


class Person4(Player):
    def __init__(self, name, age):
        self.name = name
        self.age = age



ajju = Person4("Ajju", 22)
ajju.print_sp_details()  # Person4 inherits Player, Player inherits Sportsman
print(ajju.plays)







