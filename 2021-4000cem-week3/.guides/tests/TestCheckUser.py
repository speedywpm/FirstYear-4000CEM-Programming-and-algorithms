import sys

f1 = open("CheckUser.py")
f2 = open(".guides/tests/BetterCheckUser.py")
contents1 = f1.read()
contents2 = f2.read()
f1.close()
f2.close()

lines1 = contents1.split("\n")
lines2 = contents2.split("\n")
if len(lines1)!=len(lines2):
  print("Number of lines in CheckUser.py changed.")
  print("There should be 6 lines.")
  sys.exit(1)

if lines1[0][0]!="#":
  print("Line 1 has changed - it should not have.")
  sys.exit(1)
if lines1[1][0]!="#":
  print("Line 2 has changed - it should not have.")
  sys.exit(1)
if lines1[2].count("(") != 1:
  print("Line 3 needs ONE pair of parentheses")
  sys.exit(1)  
if lines1[3].count("(") != 1:
  print("Line 4 needs ONE pair of parentheses")
  sys.exit(1)  
if lines1[4].count("(") != 0:
  print("Line 5 needs NO parentheses")
  sys.exit(1)  
if lines1[5].count("(") != 2:
  print("Line 6 needs TWO pair of parentheses")
  sys.exit(1)  

  

sys.exit(0)