def power(n,p):
  """Raises n to power p.  Input n is any number and p a non-negative integer."""  
  if p==0:
    return 1 
  else:
    ans=n*power(n,p-1)
    return ans
