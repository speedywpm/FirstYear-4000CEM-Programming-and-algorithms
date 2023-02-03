
def personalAllowance(salaryint):
  allowance=12500
  if salaryint>100000 and salaryint%2==0 and (12500-((salaryint-100000)*0.5))>=0:
    allowance=12500-((salaryint-100000)*0.5)
    return int(allowance)
  elif salaryint>100002 and salaryint%2==1 and (12500-((salaryint-100000)*0.5))>=0:
      allowance=12500-((salaryint-100000)*0.5)+1
      #print("hey")
      return int(allowance)
  elif (12500-((salaryint-100000)*0.5))<=0:
      allowance=0
      return int(allowance)
  else:
      allowance=12500
      #print("im here")
      return int(allowance)
    #elif salaryint<=0:
      #allowance=0
      #else:
         # "your salary can not be negative"
    
def nationalInsurance(salaryint):
  if salaryint<=183:
    payment=183*0
    #print("block1")
    return int(round(payment, 0))
  elif salaryint>183 and salaryint<962:
    payment=(salaryint-183)*0.12
    #print("block2")
    return int(round(payment, 0))
  elif salaryint>962:
    payment=(962-183)*0.12+((salaryint-962)*0.02)
    #print("block3")
    return int(round(payment, 0))
  else:
    #print("block4")
    pass

  
def incomeTax(salaryint):
    termp=personalAllowance(salaryint)
    if salaryint>=0 and salaryint<=37500 and salaryint<=personalAllowance(salaryint):
      itx=0
      #print("block0")
      return itx
    elif salaryint>=0 and salaryint<=37500:
      pallow=personalAllowance(salaryint)
      ama=int(salaryint)-int(pallow)
      itx=int(round(ama*0.2, 0))
      #print("block1")
      return int(itx)
    elif salaryint>37500 and salaryint<150000 and salaryint-personalAllowance(salaryint)>=37500:
      alli=salaryint-personalAllowance(salaryint)-37500
      #malli=alli-37500
      #balli=alli-malli
      itx=int(round((37500*0.2)+(alli*0.4),0))
      return itx
    elif salaryint>37500 and salaryint<150000 and salaryint-personalAllowance(salaryint)<37500:
      walle=salaryint-personalAllowance(salaryint)
      itx=int(round(walle*0.2, 0))
      return itx
    #elif salaryint>37500 and salaryint<150000:
      #pallow=personalAllowance(salaryint)
      #aida=salaryint-37500
      #ama=37500-pallow
      #itx=int(round((ama*0.2)+(aida*0.4),0))
      #print("block2")
      #return itx
    else:
      aida=salaryint-37500-112500
      itx=int(round((37500*0.2)+(112500*0.4)+(aida*0.45),0))
      #print("block3")
      return itx
    
#salary = input("What is your salary?")
#salaryint = int(salary)
#print("Your allowance is "+str(personalAllowance(salaryint))+"£")
#print("Your NI TAX is: "+ str(nationalInsurance(salaryint))+"£")
#print("Your income tax is "+str(incomeTax(salaryint))+"£")