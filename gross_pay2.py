#Calculating the gross pay with 1.5 times the hourly rate four hours worked above 40 hours:

#Asking the User the hours and rate 
string_hours = input("Enter the hours worked: ")
string_rate = input("Enter the rate: ")

#Converting to float
float_hours = float(string_hours)
float_rate = float(string_rate)

#Calculating the gross pay
if(float_hours > 40):
  hours_above = float_hours - 40
  rate_above = float_rate * 1.5
  pay = (float_rate * 40) + (hours_above * rate_above)
else:
  pay = float_hours * float_rate

#Printing the result
print("The gross pay is {}".format(pay))

