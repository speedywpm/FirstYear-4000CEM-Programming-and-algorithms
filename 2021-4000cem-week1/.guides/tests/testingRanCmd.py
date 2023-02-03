import sys

f = open('/home/codio/.bash_history')
history = f.read()
f.close()

if "python3 hello.py" in history:
  print("Command was found in terminal history.")
  sys.exit(0)
else:
  print("Command not found in terminal history.")
  sys.exit(1)
  
