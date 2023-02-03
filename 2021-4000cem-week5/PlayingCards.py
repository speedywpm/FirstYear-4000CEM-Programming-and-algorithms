# Code to create a list of 52 strings, each representing one playing card
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
deck=[]
for S in suits:
  for R in ranks:
    card = str(R) + " of " + S
    deck.append(card)

print(deck)