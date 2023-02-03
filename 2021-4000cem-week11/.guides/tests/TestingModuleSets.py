#!/usr/bin/python3
import sys

f1 = open("ModuleSets.py", "r")
f2 = open(".guides/tests/ModuleSetsOriginal.py", "r")
contents1 = f1.read()
contents2 = f2.read()
f1.close()
f2.close()

lines1 = contents1.split("\n")
lines2 = contents2.split("\n")
for i in range(10):
  if lines1[i] != lines2[i]:
    print("Line " + str(i+1) + " has been edited - return it to the original.")
    sys.exit(1)
for i in range(10, len(lines1)):
    for char in lines1[i]:
        if char.isdigit():
            print("Line " + str(i+1) + " contains a number - this is not allowed.")
            sys.exit(1)

sys.path.insert(0, '/home/codio/workspace')
from ModuleSets import *           
print("--------------------")

if 'ansA' not in locals():
    print("variable ans1 is not defined!")
    sys.exit(1)
if 'ansB' not in locals():
    print("variable ans1 is not defined!")
    sys.exit(1)
if 'ansC' not in locals():
    print("variable ans1 is not defined!")
    sys.exit(1)
    
if ansA != {'120CT', '122COM', '106CR', '121COM', '104KM', '124MS'}:
    print("ansA is incorrect")
    sys.exit(1)
if ansB != {'121COM'}:
    print("ansB is incorrect")
    sys.exit(1)    
if ansC != {'104KM', '106CR'}:
    print("ansC is incorrect")
    sys.exit(1)
    
print("All tests passed")
sys.exit(0)