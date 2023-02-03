#!/usr/bin/python3
import sys
import os

# this is the file I want to test
fullPath = os.path.abspath('PowerRecursive.py') 
# I read in the file as a string
f = open(fullPath, "r")
Scode = f.read()
f.close()
# I check that there is no use of built-in power operator
if "**" in Scode:
  print("Your code uses the built-in power operator '**'.")
  print("This is against the point of the exercise.")
  print("We are looking at ways to implement that operator.")
  print("Try again without it.")
  sys.exit(1)


import random
sys.path.insert(0, '/home/codio/workspace')
from PowerRecursive import power

testN = [random.randint(-9,9) for r in range(10)]
testP = [random.randint(1,9) for r in range(10)]

for i in range(10):
  n = testN[i]
  p = testP[i]
  if power(n,p) != n**p:
    print("Failed test with function input: " + str((n,p)))
    sys.exit(1)  

if power(5,0) != 1:
  print("Failed test with function input: " + str((5,0)))
  sys.exit(1)     
    
print("Tests all passed")
sys.exit(0)
