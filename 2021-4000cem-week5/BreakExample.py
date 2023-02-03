# Interactive Adder
tot = 0
while True:
  userCommand = input("Enter next value or STOP: ")
  if userCommand=="STOP":
    break
  tot = tot + int(userCommand)

print("Total is: " + str(tot))