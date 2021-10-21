list1 = ["One", "Two", "Three", "Four"]

print(enumerate(list1).__next__())  # Returns the index and item on that index.

for index, item in enumerate(list1):
    if index % 2 == 0:
        print(item)
#  Saves the declaration of additional variable to hold index when custom printing is the requirement.
