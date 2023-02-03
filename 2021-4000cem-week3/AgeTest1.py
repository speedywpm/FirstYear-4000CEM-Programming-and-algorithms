def ageTest(age):
  if age<0:
    return False
  elif age>0:
    return True
  if age==0:
    return False
    

if __name__=="__main__":
  userNumber_str = input("Please enter your age: ")
  userNumber = int(userNumber_str)
  ageTest(userNumber)
