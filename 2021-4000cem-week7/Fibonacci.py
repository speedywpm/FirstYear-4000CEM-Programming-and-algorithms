# Write a recursive function called fib.  
# The function should take one input, n, 
#   which is assumed a positive integer.  
# It should output the nth Fibonnaci Number.
# Fn = F[n-1] + F[n-2]

def fib(n):
  if n<=2:
    Fn=1
    return Fn
  else:
    Fn=fib(n-1)+fib(n-2)
    return Fn


  