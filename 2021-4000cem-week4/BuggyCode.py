# Fix this buggy code
options = ["1. Eat an Apple", "2. World Peace", "3. Destroy the World"]
print("Here are your options:")
print(options)
x = int( input("What would you like to do? ") )
print("Ok... " + options[x-1])

# Note: It's a silly example, but a serious point.
# Such logic errors can be really hard to find and 
# have big consequences!
