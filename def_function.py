#Creating a function that calculates the gross pay with 1.5 times the hourly rate four hours worked above 40 hours:
def compute_pay(hours, rate):
  if(hours > 40):
    hours_above = hours - 40
    rate_above = rate * 1.5
    pay = (rate * 40) + (hours_above * rate_above)
  else:
    pay = hours * rate
  print("The gross pay is {}".format(pay))
  return pay

#Prompting the User the hours and rate
string_hours = input("Enter the hours worked: ")
string_rate = input("Enter the rate: ")

#Converting to float
float_hours = float(string_hours)
float_rate = float(string_rate)

#Calling the function
result = compute_pay (float_hours, float_rate)

#Result
print(result)