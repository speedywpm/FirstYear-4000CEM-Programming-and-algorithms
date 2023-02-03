# This is flawed code - the second branch can never be accessed.
def giveDiscount(age):
  if age<65 and age>18:
    print("Not an OAP - no discount")  
    out = False
  else:
    out = True
  return out
