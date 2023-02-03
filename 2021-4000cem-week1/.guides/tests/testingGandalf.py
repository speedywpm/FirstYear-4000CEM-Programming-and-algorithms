import os
import subprocess
import sys

# this is the file I want to test
fullPath = os.path.abspath('Gandalf.py') 

# I read in the file as a string
f = open(fullPath, "r")
original = f.read()
f.close()

# I overwrite with the same thing but redirect stdout to temporary file
new = "import sys \nf = open('12345temp.txt', 'w')\nsys.stdout = f\n\n" + original + "\n\nf.close()"
f = open(fullPath, "w")
f.write(new)
f.close()

# I run the new file
try:
  subprocess.call( ["python3", fullPath]) 
except:
  print("Your script produced an error message when run  - try again")
  sys.exit(1)

# I return the original file to its original state
f = open(fullPath, "w")
f.write(original)
f.close()

# I get the contents of the temporary file
f = open("12345temp.txt")
output = f.read()
f.close()

# I delete the temporary file
os.remove("12345temp.txt")

# Finally check if the students print statements are correct
lines = output.split("\n")
line1 = 'Gandalf shouted "you shall not pass!" to the monster.'
line2 = "The monster's breath was fire." 
if not(line1 in lines):
  print("The output from your script did not contain the line:")
  print(line1)
  if not(line2 in lines):
    print("The output from your script did not contain the line:")
    print(line2)
  sys.exit(1)
if not(line2 in lines):
  print("The output from your script did not contain the line:")
  print(line2)
  sys.exit(1)        
sys.exit(0)


