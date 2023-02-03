#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/codio/workspace')
from Temperature import centToFaren, farenToCent

if centToFaren(28)!=82.4:
  print("centToFaren Test failed with input: " + str(28))
  print("Expected answer 82.4")
  sys.exit(1)

if farenToCent(90.5)!=32.5:
  print("farenToCent Test failed with input: " + str(90.5))
  print("Expected answer 32.5")
  sys.exit(1)  
  
print("Tests all passed")
sys.exit(0)
