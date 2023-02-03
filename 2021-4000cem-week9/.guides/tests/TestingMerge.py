#!/usr/bin/python3
import random, copy, sys

sys.path.insert(0, '/home/codio/workspace')
fileName = "MergeSort.py"
functionName = "mergeSort"

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




class Test(object):
    def __init__(self, n, f ):
        self.name = n
        self.function = f
        self.success = False

sortingAlgorithms = [ Test('mergeSort', mergeSort)]

# ==============================================
#    This is the small collection of number tests
# ============================================== 
# generate 10 random numbers between -100 and 100 so we can see that it's working
smallNumbers = [ random.randint(-100,100) for i in range(10) ]

# print out the small numbers
print( 'SMALL SEQUENCE TEST' )
print( 'starting numbers:', smallNumbers )

# sort the small numbers
smallCorrect = sorted( smallNumbers )
print( 'correctly sorted:', smallCorrect )

for test in sortingAlgorithms:
    result = test.function( copy.copy(smallNumbers) )
    print( '%s:' % test.name.rjust(16), result )

    # record if the test was a success
    test.success = result == smallCorrect

for test in sortingAlgorithms:
    if test.success:
        print( test.name, "worked!")
    else:
        print( test.name, "failed!")
        sys.exit(1)
    
print()

# ==============================================
#    This is the big collection of numbers test
# ============================================== 
# generate 5000 random numbers so we can profile our code
bigNumbers = [ random.random() for i in range(5000) ]

print( 'BIG SEQUENCE TEST' )

# sort the big numbers
bigCorrect = sorted( bigNumbers )

for test in sortingAlgorithms:
    if not test.success:
        continue

    result = test.function(bigNumbers.copy())

    test.sucess = result == bigCorrect
    
for test in sortingAlgorithms:
    if test.success:
        print( test.name, "worked!")
    else:
        print( test.name, "failed!")
        sys.exit(1)

sys.exit(0)
