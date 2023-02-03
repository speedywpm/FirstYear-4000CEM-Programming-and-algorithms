from Printer import dictPrinter

diceDict = {}
for dice1 in range(1,7):
    for dice2 in range(1,7):
        tot = dice1+dice2
        if tot in diceDict:
            diceDict[tot].append( (dice1,dice2) )
        else:
            diceDict[tot] = [(dice1,dice2)]
    print (tot)
dictPrinter(diceDict)