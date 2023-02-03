#!/usr/bin/python3

import sys
sys.path.insert(0, '/home/codio/workspace')
fileName = "average.py"

# First check they have created the file.
try:
  f = open(fileName, "r")
except FileNotFoundError:
  print("There is no file called " + fileName + " in your main worspace.  ")
  print("Did you change the filename or delete the file?")
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
importString = "import " + fileName[:-3]
try:
  exec(importString)        
except SyntaxError as synE:
  print("Your code has a syntax error identified on line " + str(synE.lineno) + "\n")
  print("Check for missing brackets or too many brackets on this line or on the line above.")
  print("You could also try running the file yourself in the terminal for more details.")
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
except TypeError as te:
  print("")
  print("#"*10 + "\nFEEDBACK\n" + "#"*10)
  print("Your code creates a TypeError when run.  Try running the file yourself in the terminal to see this.")
  if "unsupported operand type(s) for /" in str(te):
    print("The error message Python gives is...")
    print(str(te))
    print("The message is telling is that the divide symbol is being given data of the wrong type.")
    print("Specifically - the data on the left of the / is a None type")
    print("This is most likely because the left of the / symbol is a complete print statement (after it finishes printing there is nothing left).")
    print("The division should be done BEFORE printing - check your parentheses!")
    sys.exit(1)
    
# Running code should be error free if we get here:  
# So run and save to file
original = sys.stdout
f = open('.guides/tests/out.txt', 'w')  
sys.stdout = f
exec(studentCode)
sys.stdout = original
f.close()

f = open('.guides/tests/out.txt', 'r')
output=f.read()
f.close()
print(output)

if "55.0" in output:
  print("All tests passed.")
  sys.exit(0)
elif "407.0" in output:
  print("#"*10 + "\nFEEDBACK\n" + "#"*10)  
  print("Your code does not produce any error messages.")
  print("But it states the answer as 407.0 for an average of numbers between 11 and 99!")
  print("You are most likely dividing only the last number by 9 rather than the sum.")
  print("Check your parentheses!")
  sys.exit(1)
else:
  print("your script is not printing the right answer.")
  print("Remember you need to use print followed by parentheses containing the thing you want to print.")
  sys.exit(1)




