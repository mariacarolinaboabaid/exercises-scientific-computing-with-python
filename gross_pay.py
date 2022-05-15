print("This programm that compute de gross pay")

#Asking the User the number of hours and rate
hours = input("Enter hours:  ")

rate = input("Enter rate:  ")


#Calculation
gross_pay = float(hours) * float(rate)

#Result
print("Gross Pay: {}".format(gross_pay))