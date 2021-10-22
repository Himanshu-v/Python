class Static:
    @staticmethod
    def print_something():
        print("something something hmmm?")


stat = Static()
print(stat.print_something())  # Int. Fact - Execution hierarchy is inside out. See output.
Static.print_something()