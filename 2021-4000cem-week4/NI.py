def nationalInsurance(wsalary):
  if wsalary<=183:
    payment=183*0
    return int(round(payment, 0))
  elif wsalary>183 and wsalary<962:
    payment=(wsalary-183)*0.12
    return int(round(payment, 0))
  elif wsalary>962:
    payment=(962-183)*0.12+((wsalary-(962-183))*0.02)
    return int(round(payment, 0))
  