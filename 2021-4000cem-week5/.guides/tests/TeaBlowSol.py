temp = 100
blow=0
print("After " + str(blow) + " blows the tea is " + str(round(temp,2)))
while temp > 70:
  blow = blow+1
  temp = temp*(90/100)
  print("After " + str(blow) + " blows the tea is " + str(round(temp,2)))

