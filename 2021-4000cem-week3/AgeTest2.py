def ageTest(age):
  if age<0:
    print("That's not possible!") 
    out = False
  else:
    print("That number makes sense.")
    out = True
  print("Thank You")
  return out

if __name__=="__main__":
  userNumber_str = input("Please enter your age: ")
  userNumber = int(userNumber_str)
  ageTest(userNumber)
