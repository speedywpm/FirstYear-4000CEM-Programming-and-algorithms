#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/codio/workspace')
from Percentage import makePercentage

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


