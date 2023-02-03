days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
count = 0
while count<7:
  day = days[count]
  print("Today is " + day)
  if day=="Friday":
    print("Woohoo!")
  count = count+1