#THIS PROGRAM WILL SHOW THE GRADE ACCORDING THE SCORE GIVEN BY THE USER:
score = input("Enter here your score that must be between 0.0 a 1.0: ")

try:
    score = float(score)
except:
    print("Bad Score, must be between 0.0 a 1.0")
    quit()

if 0 > score or score > 1.0: 
    print("Bad Score, must be between 0.0 a 1.0")
if 0.9 <= score <= 1.0:
    print("Your grade is A!")
elif score == 0.8:
    print("Your grade is B!")
elif score == 0.7:
    print("Your grade is C!")
elif score == 0.6:
    print("Your grade is D!")
elif 0 == score < 0.6:
    print("Your grade is F!")