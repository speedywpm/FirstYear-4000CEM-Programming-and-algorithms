#!/usr/bin/python3
import sys
sys.path.insert(0, '/home/codio/workspace')

from Absolute import absoluteValue

if absoluteValue(123) != 123:
  print("Failed test with function input: 123")
  sys.exit(1)
if absoluteValue(-456) != 456:
  print( type(absoluteValue(-456)) )
  print("Failed test with function input: -456")
  sys.exit(1)
if absoluteValue(0) != 0:
  print("Failed test with function input: 0")
  sys.exit(1)

print("Tests all passed")
sys.exit(0)


def safetype(val):
  s = str(type(val))
  return s.replace("<", "&lt;").replace(">", "&gt;")