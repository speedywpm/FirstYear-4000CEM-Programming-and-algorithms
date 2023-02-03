#!/usr/bin/python3

import sys
sys.path.insert(0, '/home/codio/workspace')
fileName = "Percentage.py"
functionName = "makePercentage"

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

  
# Finally - test if the function works
print("File exists; function exists; code has no syntax errors.  Testing function now...\n")




ans = 5/50*100
if makePercentage(5,50) != ans:
  print("Failed test with function input: 5, 50")
  print("Answer should be: " + str(ans))
  sys.exit(1)

ans = 9/15*100
if makePercentage(9,15) != ans:
  print("Failed test with function input: 9, 15")
  print("Answer should be: " + str(ans))
  sys.exit(1)  
  
ans = 0/70*100
if makePercentage(0,70) != ans:
  print("Failed test with function input: 0, 70")
  print("Answer should be: " + str(ans))
  sys.exit(1)  

ans = 20/20*100
if makePercentage(20,20) != ans:
  print("Failed test with function input: 20, 20")
  print("Answer should be: " + str(ans))
  sys.exit(1)
  

print("Tests all passed")
sys.exit(0)


