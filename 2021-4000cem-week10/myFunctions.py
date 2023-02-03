def howManyTimes(inList, target):
    count=0
    for i in range(len(inList)):
        entry = inList[i]
        if entry == target:
            count = count + 1
    return count
