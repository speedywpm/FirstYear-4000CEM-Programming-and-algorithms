#!/usr/bin/python3
import sys

f = open("words.txt", "r")
oneGiantString = f.read()
f.close()
myWordList = oneGiantString.split("\n") 

sys.path.insert(0, '/home/codio/workspace')
try:
    from makeWordList import *
except:
    print("File makeWordList.py creates exceptions!")
    print("Deal with these before checking solution.")
    sys.exit(1)

try:
    ll = len(wordList)
    if ll!=113809:
        print("The word list should have 113809 elements but has " + str(ll) )
        sys.exit(1)
    ele1 = wordList[0]
    if ele1!="aa":
        print("The first element of the list should be 'aa' but is " + str(ele1))
        sys.exit(1)
except:
    print("Could not measure length or access first element of wordList")
    sys.exit(1)

if myWordList!=wordList:
    print("wordList is incorrect - did you edit words.txt?")
    sys.exit(1)  
    
print("Tests passed")
sys.exit(0)
