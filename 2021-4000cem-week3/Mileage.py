def milageClaim(miles):
  
  # Write the function body here.  Use as many lines as needed.
  # You code should create variable claim so the return statement works. 
  expense=0
  if miles>0:
    expense=0
    if miles==0:
      expense=0
    elif miles<=10:
      expense=miles*0.50
    elif miles>10 and miles<100:
      miles=miles-10
      expense=10*0.50+(miles*0.37)
    else:
      miles=miles-100
      expense=10*0.50+(90*0.37)
      
  return expense

if __name__=="__main__":
    miles = int(input("How many miles? "))
    print("Claim is for £" + str( round(milageClaim(miles), 2) ))