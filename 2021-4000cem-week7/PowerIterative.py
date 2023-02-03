n=0
p=0
def power(n,p):
  """Raises n to power p.  Input n is any number and p a non-negative integer."""
  ans = 1
  for i in range(1,p+1):
    ans = ans*n
  return ans

print(power(3,0))


