#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/codio/workspace')
from Weight import imperialToMetric, metricToImperial

in1 = 14
in2 = 7
Sans = imperialToMetric(in1,in2)
if Sans != 92.075:
  print("imperialToMetric Test failed with input: " + str((in1,in2)))
  print("Expected answer 92.075")
  print("Recieved answer: " + str(Sans) )
  sys.exit(1)

if metricToImperial(90)!=(14,2):
  print("metricToImperial Test failed with input: " + str(90))
  print("Expected answer (14,2)")
  sys.exit(1)  
  
print("Tests all passed")
sys.exit(0)
