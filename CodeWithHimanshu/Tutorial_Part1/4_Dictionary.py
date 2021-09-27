dict1 = {"name": "Himanshu", "age": 25,
         "interests": ["singing",
                       {"dictInList": "youCan",
                        "canTuple": ('yes', 'whatnot',
                                     {"dictInTuple": "youCan",
                                      })
                        }
                       ]
         }
print(dict1["interests"][1]["canTuple"][2]["dictInTuple"])

# Adding values in dictionary.

dict1["newlyAdded"] = 12234
dict1[142*10] = "numberKeysAreAllowed"  # inline operations are allowed.
dict1[142/10] = "FloatKeysAreAllowed"
dict1.update({'added': 'withUpdate'})  # Insert using update method.
dict1.update({'name': 'Updated'})  # Change value using update method.

print(dict1)

# removing elements
del dict1[14.2]
print(dict1)

# COPYING
dict2 = dict1  # Deep copy, both pointers referring to the same structure
del dict2['age']
print(dict1)  # Any change on the copy will reflect in the original dict.

dict3 = dict2.copy()  # Shallow copy.
del dict3['name']
print(dict3)
print(dict2)  # No change in the original.

dict1.__format__()


