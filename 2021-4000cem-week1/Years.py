# Script to ask the user for a year and works out how many days
yearStr = input("How many years old are you? ")
yearInt = int(yearStr)
inDays = yearInt*365
print("That is " + str(inDays) + " days!")