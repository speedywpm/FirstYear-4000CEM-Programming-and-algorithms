tot = 0
while tot<=100:
  x = int( input("How much is the next item? ") )
  tot = tot+x
print("You cannot afford that!  You only have £" + str(100-(tot-x)) + " left.")
