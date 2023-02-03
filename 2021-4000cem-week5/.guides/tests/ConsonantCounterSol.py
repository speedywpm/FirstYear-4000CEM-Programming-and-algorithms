def consonantCounter(text):
  """Count the number of consonant in a word entered as string"""
  # Write the Function Body!
  c = 0
  for letter in text:
	  if letter in "bcdfghjklmnpqrstuvwxyz" or letter in "bcdfghjklmnpqrstuvwxyz".upper():
      c = c + 1
  return(c)
