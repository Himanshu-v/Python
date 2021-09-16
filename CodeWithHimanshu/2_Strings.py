# TUT8
# STRINGS
# SLICING
myStr = "Himanshu"
print(myStr)
# myStr[INCLUSIVE_START:EXCLUSIVE_END]
print(myStr[:])
print(myStr[3:6])
print(myStr[0:])
print(myStr[:6])

# EXTENDED SLICING # myStr[INCLUSIVE_START:EXCLUSIVE_END:STEPS]
print(myStr[:6:3])
print(myStr[::2])  # Skip 2-1 chars.
print(myStr[::-1])  # Reverse
print(myStr[::-2])  # steps <-1 with default start and end works as expected
print(myStr[1:6:-2])  # steps <-1 with start and end index doesn't work as expected. So don't use -ve step <-1

print(myStr)  # Strings are immutable.

# FUNCTIONS
print(myStr.isalnum())  # True is the string does have only alphanumeric characters, AC = either a letter or number.
print(myStr.isalpha())  # True is the string does have only alphabets characters.
print(myStr.find("hu"))  # matches the word and returns the index of first letter.

# manymore functions are there.
