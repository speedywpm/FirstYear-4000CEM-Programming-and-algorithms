try:
    # Script to evenly distribute
    n = input("How many people? ")
    pc = 100/int(n)
    print("Everyone gets " + str(pc) + "%")
except ZeroDivisionError:
    print("No one gets anything")
except ValueError:
    print("Unacceptable Input")
