import sys

# I read in the student file as a string
f = open("SpendCheck.py", "r")
student = f.read()
f.close()

# I read in my solution file as a string
f = open(".guides/tests/SpendCheckSol.py", "r")
mine = f.read()
f.close()

# Check lines 3-5 are the same
studentL = student.split("\n")
mineL = mine.split("\n")
for line in [3,4,5]:
  if studentL[line-1]!=mineL[line-1]:
    print("You changed line " + str(line) + ".  This was not instructed.")
    sys.exit(1)

# Check the edit line 1 correctly

sline = studentL[0]
sline = sline.split('#',1)[0] # Remove comments at end of line
sline = sline.replace(" ", "")  # remove whitespace
myline = "tot=0"
if sline != myline:
  print("Line 1 should initialise the variable tot to zero")
  sys.exit(1)

# Check they edit line 2 correctly
sline = studentL[1]
sline = sline.split('#',1)[0] # Remove comments at end of line
sline = sline.strip()# remove trailing whitespace
sline = sline.replace("tot ", "tot")  # remove whitespace around comparison
sline = sline.replace("<=", "<")  # I except <= or <
sline = sline.replace("< ", "<")  # remove whitespace around comparison
if sline[-1]!=":":
  print("Forgot colon!")
  sys.exit(1)
options = ["while tot<100:",  
           "while (tot<100):"]
if not(sline in options):
  print("Line 2 should check tot is less than 100")
  sys.exit(1)  

print("Code is correct")
sys.exit(0)
