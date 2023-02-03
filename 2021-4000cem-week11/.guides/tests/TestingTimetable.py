#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/codio/workspace')
from Timetable import whatNow

timetable = { ("Mon",9):"121COM", ("Mon", 3):"A.L.L.", ("Wed", 10):"121COM"} 

if whatNow("Mon", 3) != "A.L.L.":
  print("Failed test with input in timetable")
  sys.exit(1)

try:
    out = whatNow ("Tue", 4)
except KeyError:
    print("Key Error triggered by input not in timetable.  Try again!")
    sys.exit(1)
if out != "Free!":
  print("Failed test with input not in timetable")
  print("Expected 'Free!' but got: " + str(out))
  sys.exit(1)
  
print("Tests all passed")
sys.exit(0)
