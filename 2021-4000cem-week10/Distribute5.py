try:
    n = input("How many people? ")
    pc = 100/int(n)
    print("Everyone gets " + str(pc) + "%")
except:
    print("Something bad happened!")
