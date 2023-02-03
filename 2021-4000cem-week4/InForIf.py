allowedAccess=["Alice", "Bob", "Eve"]
name = input("What is your name? ")
if name in allowedAccess:
	print("Welcome in!")
else:
	print("No access!")
