def factorial(n):
  '''Iterative function to compute factorial of positive integer n.'''
  ans = 1
  a=n
  while a>=1:
    ans = ans * a
    a=a-1
  return ans
