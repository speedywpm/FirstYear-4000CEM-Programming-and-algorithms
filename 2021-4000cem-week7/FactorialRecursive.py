def factorial(n):
  '''Recursive function to compute factorial of positive integer n.'''
  if n == 0:
    return 1
  else:
    ans = n*factorial(n-1)
    return ans
