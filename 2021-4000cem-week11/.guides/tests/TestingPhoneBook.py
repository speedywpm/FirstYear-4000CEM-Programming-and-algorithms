#!/usr/bin/python3
import sys

f1 = open("PhoneBook.py", "r")
f2 = open(".guides/tests/PhoneBookOriginal.py", "r")
contents1 = f1.read()
contents2 = f2.read()
f1.close()
f2.close()

lines1 = contents1.split("\n")
lines2 = contents2.split("\n")
for i in range(7):
  if lines1[i] != lines2[i]:
    print("Line " + str(i+1) + " has been edited - return it to the original.")
    sys.exit(1)
for i in range(18, len(lines1)):
    for char in lines1[i]:
        if char.isdigit():
            print("Line " + str(i+1) + " contains a number - this is not allowed.")
            sys.exit(1)

sys.path.insert(0, '/home/codio/workspace')
from PhoneBook import *           
print("--------------------")

try:
    if myContacts["Bran Stark"] != myContacts["Jon Snow"]:
        print("Key 'Bran Stark' does not make to the same value as key 'Jon Snow'") 
        sys.exit(1)
except KeyError:
    print("Key 'Bran Stark' is not in the dictionary!")
    sys.exit(1)

try:
    if myContacts["Jaime Lannister"] != myContacts["Cersei Lannister"]:
        print("Key 'Jaime Lannister' does not make to the same value as key 'Cersei Lannister'")
        sys.exit(1)
except KeyError:
    print("Key 'Jaime Lannister' is not in the dictionary!")
    sys.exit(1)

if "Ned Stark" in myContacts:
    print("Ned Stark is still in the dictionary!")
    sys.exit(1)

print("All tests passed")
sys.exit(0)