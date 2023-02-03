def numToDay(n):
    """Input is int between 1-7.  Output is corresponding day as 3 letter string"""
    Mtup = (" ", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    if n>7:
        raise ValueError("There are only 7 days!")
    else:
        return(Mtup[n])

#print(numToDay(4))
print("")
print(numToDay("8"))
