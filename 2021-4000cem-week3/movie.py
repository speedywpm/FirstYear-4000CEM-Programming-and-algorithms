def movie(age):
  if age<12:
    print("You're too young to watch this movie.") 
    return None
  else:
	  price=15
	  if age>65:
		  discount=10
	  elif age<18:
		  discount=20
	  else:
		  discount=0
	  price = 15/100*(100-discount)
	  return price

print(movie(100))