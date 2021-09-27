s = set()
s.add(1)
s.add(2)
print(s)
s.remove(2)
print(s)

#  Set from List.

setFList = set([1, 2, 3])
print(setFList)
unionSet = s.union(setFList)
intSet = s.intersection(setFList)
print(unionSet)
print(intSet)
