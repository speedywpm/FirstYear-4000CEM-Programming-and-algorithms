def power(n,p):
  """Raises n to power p.  Input n is any number and p a non-negative integer.""" 
  # We put in a check to make sure p is an integer.
  if type(p)!=int or p<0:
    print("Function power has been called with input (n,p) = " + str((n,p)) )
    raise TypeError("The power p must be a non-negative integer.")
  # The base case is still p=0
  if p==0:
    return 1 
  # Do not edit code above here!
  # ----------------------------
  # You need to write code below which contains the recursive calls.
  # It will take several lines.  
  # Remember that there are two cases - odd and even
