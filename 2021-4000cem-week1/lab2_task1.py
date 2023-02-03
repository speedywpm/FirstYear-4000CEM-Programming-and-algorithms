yearsstr = input("insert time in years")
years = int(yearsstr)
poundsstr = input("insert desired investment ammount")
pounds = int(poundsstr)
intereststr = input("insert interest per year")
interest = int(intereststr)
y=pounds*(1+(interest/100))**years
print(y)
  