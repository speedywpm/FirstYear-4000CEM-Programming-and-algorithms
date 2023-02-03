def countdown(n):
  '''Function to countdown to blastoff from positive integer'''
  if n <= 0:
    print("Blastoff!")
  else:
    print(n)
    countdown(n-1)

countdown(3)