#!/usr/bin/python3

import sys, random

sys.path.insert(0, '/home/codio/workspace')
fileName = "Locate.py"
functionName = "locate"

# First check they have created the file.
try:
    f = open(fileName, "r")
except FileNotFoundError:
    print("There is no file called " + fileName + " in your main worspace.  ")
    print("Please check the spelling in your file name - it must be the right case")
    sys.exit(1)

# Next check they are not using import.
f = open(fileName, "r")
studentCode = f.read()
f.close()
if studentCode.find("import ")!=-1:
    print("You are not allowed to import other code for this task.")
    print("You must write the code all by yourself!  Try again.")
    sys.exit(1)

# Now test that their code is free of syntax errors, and that the function exists
importString = "from " + fileName[:-3] + " import " + functionName
try:
    exec(importString)
except SyntaxError as synE:
    print("Your code has a syntax error identified on line " + str(synE.lineno) + "\n")
    print("Check for missing colons (:) and missing indentation.")
    print("Check for missing brackets (these may be missing on the line above).")
    print("Try running yourself in the terminal for more details.")
    sys.exit(1)
except ImportError:
    print("The file exists but there is no function called " + functionName + " defined inside.")
    print("Please check the spelling in your function name - it must be the right case")  
    sys.exit(1)
except EOFError:
    print("")
    print("")
    print("Your code cannot be tested because it contains an input statement.")
    print("")
    print("The code is waiting for someone to type at the keyboard - this is not how the Codio tests work.")
    print("Your functions should only rely on arguments and returns to communicate.")
    print("Personal test code must be commented out before running Codio tests.")
    print("Hence please comment out the input statement and test again.")
    sys.exit(1)

# Finally - test if the function works
print("File exists; function exists; code has no syntax errors.  Testing function now...\n")

sequence = [random.randint(0, 1000) for i in range(100)]
sequence.sort()
print("Testing Sequence Generated:  Random integers in ascending order:")
print(sequence)

testIn = [random.randint(0, 1000) for i in range(3)]
testIn.extend( [sequence[0], sequence[20], sequence[50], 1002] )
def findAnswer(num): 
    try: 
        return sequence.index(num) 
    except:
        return None 

testOut = list(map(findAnswer, testIn))

for i in range(len(testIn)):
    try:
        testArg = testIn[i]
        studentAns = eval(functionName + "(sequence, testArg)")
    except Exception as runE:
        print("Running your function with input: " + str(testArg))
        print("created a runtime error of type: " + str(type(runE)) )
        print("Run this example yourself in the terminal for more details.")
        sys.exit(1)
    if studentAns != testOut[i]:
        print("Function failed test when searching for: " + str(testArg))
        print("Expected: " + str(testOut[i]) )
        print("Received: " + str(studentAns) )
        sys.exit(1)
    
print("All tests passed.")
sys.exit(0)

