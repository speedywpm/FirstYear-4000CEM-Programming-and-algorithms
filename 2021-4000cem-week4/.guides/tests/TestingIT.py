#!/usr/bin/python3

import sys
sys.path.insert(0, '/home/codio/workspace')
fileName = "UKTax.py"
functionName = "incomeTax"

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

testIn =  [ 0, 9000,  12500]
testOut = [ 0, 0,     0]
for i in range(len(testIn)):
  try:
    testArg = testIn[i]
    studentAns = eval(functionName)(testArg)
  except Exception as runE:
    print("Running your function with input: " + str(testArg))
    print("created a runtime error of type: " + str(type(runE)) )
    print("Run this example yourself in the terminal for more details.")
    sys.exit(1)
  if studentAns != testOut[i]:
    print("Function failed test with input: " + str(testArg))
    print("Expected: " + str(testOut[i]))
    print("Received: " + str(studentAns))
    print("Remember - if someone's salary is less than their personal allowance then they pay no income tax.")
    sys.exit(1)
    
testIn =  [ 15000, 20000, 40000]
testOut = [ 500,   1500,  5500]
for i in range(len(testIn)):
  try:
    testArg = testIn[i]
    studentAns = eval(functionName)(testArg)
  except Exception as runE:
    print("Running your function with input: " + str(testArg))
    print("created a runtime error of type: " + str(type(runE)) )
    print("Run this example yourself in the terminal for more details.")
    sys.exit(1)
  if studentAns != testOut[i]:
    print("Function failed test with input: " + str(testArg))
    print("Expected: " + str(testOut[i]))
    print("Received: " + str(studentAns))
    print("Have you remembered to only tax the taxable salary (i.e. subtracted the personal allowance)?")
    sys.exit(1)    

testIn =  [ 55000, 100000]
testOut = [ 9500,  27500]
for i in range(len(testIn)):
  try:
    testArg = testIn[i]
    studentAns = eval(functionName)(testArg)
  except Exception as runE:
    print("Running your function with input: " + str(testArg))
    print("created a runtime error of type: " + str(type(runE)) )
    print("Run this example yourself in the terminal for more details.")
    sys.exit(1)
  if studentAns != testOut[i]:
    print("Function failed test with input: " + str(testArg))
    print("Expected: " + str(testOut[i]))
    print("Received: " + str(studentAns))
    print("Remember - the higher rate tax is only applied to taxable salary OVER 37500.  The salary under is still taxed at the lower rate.")
    sys.exit(1)      

testIn =  [ 110000, 145000]
testOut = [ 33500, 50500]
for i in range(len(testIn)):
  try:
    testArg = testIn[i]
    studentAns = eval(functionName)(testArg)
  except Exception as runE:
    print("Running your function with input: " + str(testArg))
    print("created a runtime error of type: " + str(type(runE)) )
    print("Run this example yourself in the terminal for more details.")
    sys.exit(1)
  if studentAns != testOut[i]:
    print("Function failed test with input: " + str(testArg))
    print("Expected: " + str(testOut[i]))
    print("Received: " + str(studentAns))
    print("Tip: Check you have passed all the personal allowance tests.")
    sys.exit(1)

testIn =  [ 160000, 1000000]
testOut = [ 57000, 435000]
for i in range(len(testIn)):
  try:
    testArg = testIn[i]
    studentAns = eval(functionName)(testArg)
  except Exception as runE:
    print("Running your function with input: " + str(testArg))
    print("created a runtime error of type: " + str(type(runE)) )
    print("Run this example yourself in the terminal for more details.")
    sys.exit(1)
  if studentAns != testOut[i]:
    print("Function failed test with input: " + str(testArg))
    print("Expected: " + str(testOut[i]))
    print("Received: " + str(studentAns))
    print("Remember:  For people earning above 150k their income is subject to three diffeent tax rates.")
    sys.exit(1)     
    
# Finally - secret tests
testIn =  [ 0, 9000,  12500, 15000, 20000, 40000, 55000, 100000, 110000, 145000, 160000, 1000000]
testOut = [ 0, 0,     0,     500,   1500,  5500,  9500,  27500,  33500,  50500,  57000,  435000]
for i in range(len(testIn)):
  try:
    testArg = testIn[i]
    studentAns = eval(functionName)(testArg)
  except Exception as runE:
    print("Running your function with input: " + str(testArg))
    print("created a runtime error of type: " + str(type(runE)) )
    print("Run this example yourself in the terminal for more details.")
    sys.exit(1)
  if studentAns != testOut[i]:
    print("Function failed on one of the hidden tests.  Talk to a teacher.")
    sys.exit(1)     
    
print("All tests passed.")
sys.exit(0)
