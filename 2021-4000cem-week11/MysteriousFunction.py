def mysterious(filename):
    """Takes a string with a filename as input and..."""
    f = open(filename, "r")
    for line in f:
        text = line[0:-1]
        text = (60-len(text))*" " + text
        print(text)
    f.close()

mysterious("BoringTextFile.txt")