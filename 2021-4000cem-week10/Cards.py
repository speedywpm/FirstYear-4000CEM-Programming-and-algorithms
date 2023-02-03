from myFunctions import howManyTimes

myHand = ["Two","Two","Nine","Nine","Ace"]

for card in ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten", "Jack", "Queen", "King", "Ace"]:
    ans = howManyTimes(myHand, card)
    print( " "*(5-len(card)) + str(card) + " : " + str(ans) )