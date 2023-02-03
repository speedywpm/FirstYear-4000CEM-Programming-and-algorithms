def isPrime(num):
  """ The function returns True if num is prime and False otherwise""" 
  k=2
  while k>0:
    if num%2==0 or num%3==0:
      return False
    if num%1==0 and num%num==0 and (num%2>0):
      return True
  # Use a loop to check if any smaller numbers divide num (have zero remainder)

# we need to process numbers 2,3,4,5,...,num-1
for i in range(2,num)

i = 2
while i<num:
  i = i+1
  
