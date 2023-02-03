try:
    # Script to evenly distribute
    n = input("How many people? ")
    pc = 100/int(n)
    print("Everyone gets " + str(pc) + "%")
except ZeroDivisionError:
    print("No one gets anything")
except ValueError as err:
    print("You triggered a ValueError with message: ")
    print(err)
print("Hello!")
