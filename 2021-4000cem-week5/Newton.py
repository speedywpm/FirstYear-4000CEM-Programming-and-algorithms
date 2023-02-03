
def mySqrt(x):
  # missing blue square
  if ((y**2)-0.001)<y**2 and y**2<((y**2)+0.001):
    return y
  else:
    y=(y+x/y)/2
    return False
  # Write your code here.  It will need several lines including a loop!
#x=int(input("enter a positive x"))

a=mySqrt(x)
while a==False:
    y=(x+1)/2
    mySqrt(x)
    
    
