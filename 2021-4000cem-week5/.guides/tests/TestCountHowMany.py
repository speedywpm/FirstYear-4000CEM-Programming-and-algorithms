#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/codio/workspace')
from CountHowMany import howManyTimes

if howManyTimes([1,3,4,3,2], 1) != 1:
  print("Failed test with function input: [1,3,4,3,2], 1")
  sys.exit(1)
if howManyTimes([1,2,3,4,3,2], 3) != 2:
  print("Failed test with function input: [1,3,4,3,2], 3")
  sys.exit(1)
if howManyTimes(["a","b","c"], "d") != 0:
  print("Failed test with function input: ['a','b','c'], 'd'")
  sys.exit(1)
  
print("Tests all passed")
sys.exit(0)
