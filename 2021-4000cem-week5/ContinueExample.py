# Script to compute values of 1/n^3
for num in range(-10,10):
    if num==0:
        continue
    print( round(1/num**3, 5) )

