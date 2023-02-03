#!/usr/bin/python3
import sys

f = open(".guides/tests/myWords2.txt", "r")
correctGiantString = f.read()
f.close()

try:
    f = open("words2.txt", "r")
    studentGiantString = f.read()
    f.close()
except:
    print("Could not open file words2.txt")
    print("At least make the file before testing it!")
    sys.exit(1)

if "aardvarks" in studentGiantString:
    print("The word `aardvarks` is still present!")
    sys.exit(1)

nlines = len( studentGiantString.split("\n") )
if nlines!=81368 and nlines!=81369:
    print("Expected 81368 lines (=words) but words2.txt has " + str(nlines))
    sys.exit(1)    
    
if studentGiantString==correctGiantString:
    print("Correct!")
    sys.exit(0)
elif studentGiantString==correctGiantString+"\n":
    print("Correct!")
    sys.exit(0)
else:
    print("Incorrect - did you edit words.txt?")
    sys.exit(1)
  