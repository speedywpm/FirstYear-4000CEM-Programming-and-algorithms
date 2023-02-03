try:
    # Script to evenly distribute
    n = input("How many people? ")
    pc = 100/int(n)
    print("Everyone gets " + str(pc) + "%")
except (ZeroDivisionError, ValueError):
    print("Unacceptable Input")
