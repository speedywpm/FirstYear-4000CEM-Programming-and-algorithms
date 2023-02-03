# Degrees in Centigrade (C) can be converted to Fahrenheit (F) using the formula
# F = 1.8 x C + 32
# Write two functions in this file: 
# - centToFaren which takes Centigrade as input and returns Fahrenheit;
# - farenToCent: which takes Farenheit as input and returns Centigrade.
# You must use these function names for the tests to work in the Codio Guide.
koo=50
def centToFaren(A):
  f=1.8*A+32
  return(f)
x=centToFaren(koo)
print(str(x)+"    "+str(koo))
def farenToCent(F):
  """F-32=1.8c"""
  d=(F-32)/1.8
  return(d)

