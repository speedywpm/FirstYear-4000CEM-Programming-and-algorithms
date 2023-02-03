#!/usr/bin/python3
import sys
import pickle

try:
    f = open("PickledWordList.pkl", "rb")
    unpickledWL = pickle.load(f)
    f.close()
except:
    print("Could not pickle.load file PickledWordList.pkl")
    sys.exit(1)

f = open("words.txt", "r")
oneGiantString = f.read()
f.close()
myWordList = oneGiantString.split("\n") 
if myWordList!=unpickledWL:
    print("wordList unpickled but incorrect - did you edit words.txt?")
    sys.exit(1)
else:
    print("Tests passed")
    sys.exit(0)