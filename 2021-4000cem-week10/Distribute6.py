f = open("out.txt", "w")
print("File Open")
try:
    n = input("How many people? ")
    pc = 100/int(n)
    f.write(str(pc))
except ZeroDivisionError:
    print("No one gets anything")    
finally:
    f.close()
    print("File closed")
