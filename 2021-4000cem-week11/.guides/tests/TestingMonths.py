#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/codio/workspace')
from Months import numToMonth

if numToMonth(8) != "August":
  print("Failed test with function input: 8")
  sys.exit(1)
if numToMonth(12) != "December":
  print("Failed test with function input: 12")
  sys.exit(1)
  
print("Tests all passed")
sys.exit(0)
