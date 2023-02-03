#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/codio/workspace')
from CompareFiles import compare

try:
    ans = compare("BoringTextFile.txt", "BoringTextFile.txt")
except:
    print("Running function causes exceptions.")
    sys.exit(1)    
if ans!=0:
    print("Did not identify same files")
    sys.exit(1)
    
try:    
    ans = compare("BoringTextFile.txt", "DifferentBoringTextFile-SameLength.txt")
except:
    print("Running function causes exceptions.")
    sys.exit(1)
if ans!=4:
    print("Did not identify correct line where different files of same length first differ")
    sys.exit(1)   
try:    
    ans = compare("BoringTextFile.txt", "DifferentBoringTextFile-ExtraLine.txt")
except:
    print("Running function on files of different length causes exceptions.")
    sys.exit(1)
if ans!=6:
    print("Did not identify that one file had more lines")
    sys.exit(1)

print("Tests all passed")
sys.exit(0)
