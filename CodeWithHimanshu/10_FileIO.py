""" MODES OF WORKING WITH FILE
r - read (default)
w - write
x - exclusive create
t - text (default)
b - binary
+ - r+w
a - append
"""
import flask

filePointer = open("WorkingFIle.txt", 'r')
content = filePointer.read()
print(content)
filePointer.close()

"""
filePointer = open("WorkingFIle.txt", 'a')
filePointer.write("Himanshu will change the world in a positive way\n")
# filePointer.close()
"""
filePointer = open("WorkingFIle.txt", 'rt')
content = filePointer.read(8)
print(content)

for line in content:  # For printing character-by-c content.
    print(line)

for line in filePointer:  # For printing line-by-line content
    print(line)
filePointer.close()

#  Read/Text mode
filePointer = open("WorkingFIle.txt", 'rt')
# Work only until the filePointer is not read.
print(filePointer.readline())  # Reading and printing the first line
print(filePointer.readline())  # Reading Printing the next line
print(filePointer.readlines())  # To make a list of all the lines in the file.

#  Write mode
filePointer = open("NewFile.txt", 'w')
filePointer.write("Himanshu will change the world in a positive way\n")
filePointer.close()

#  Append mode
filePointer = open("NewFile.txt", 'a')
n = filePointer.write("Appended line")
print("number of chars added", n)
filePointer.close()

#  Read+Write mode
filePointer = open("NewFile.txt", 'r+')
n = filePointer.write("Write in r+ mode line")
print("read in r+ mode:", filePointer.read())
print("number of chars added", n)
print("Handle is at:", filePointer.tell())  # Prints the current handle location
print(filePointer.seek(10))  # Reset the handle
print("Handle is at:", filePointer.tell())

filePointer.close()


# MORE ON FILES.






