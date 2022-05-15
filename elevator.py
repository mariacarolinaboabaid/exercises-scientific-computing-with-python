print("This programm will do the conversion of the elevator floor")

#Getting the elevator floor in European pattern
europe_floor = input("Europe floor?:  ")

#Converting to the American pattern 
us_floor = int(europe_floor) + 1

#The result
print("Us floor: {}".format(us_floor))