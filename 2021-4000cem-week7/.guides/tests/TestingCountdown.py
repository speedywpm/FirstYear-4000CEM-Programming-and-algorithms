import sys
sys.path.insert(0, '/home/codio/workspace')

# Redirect stdout to files                                     
saveOutLocation = sys.stdout  

f = open('.guides/tests/out1.txt', 'w')                             
sys.stdout = f
from Countdown1 import countdown
countdown(3)
f.close()

f = open('.guides/tests/out2.txt', 'w')                             
sys.stdout = f
from Countdown2 import countdown
countdown(3)
f.close()

sys.stdout = saveOutLocation                                   

f1 = open('.guides/tests/out1.txt', 'r')
f2 = open('.guides/tests/out2.txt', 'r')
text1 = f1.read()
text2 = f2.read()
f1.close()
f2.close()
if text1 != text2:
  print("What is printed by Countdown1.py is not identical to what is printed by Countdown2.py")
  sys.exit(1)

print("Tests passed")
sys.exit(0)