#THIS PROGRAM WILL SHOW THE GRADE ACCORDING THE SCORE GIVEN BY THE USER

#DEFINING THE FUNCTION:
def calculation_score(score_number):
    try:
       score_number = float(score)
    except:
       print("Bad Score, must be between 0.0 a 1.0")
       quit()

    if 0 > score_number or score_number > 1.0: 
        print("Bad Score, must be between 0.0 a 1.0")
    if 0.9 <= score_number <= 1.0:
        print("Your grade is A!")
    elif score_number == 0.8:
        print("Your grade is B!")
    elif score_number == 0.7:
        print("Your grade is C!")
    elif score_number == 0.6:
        print("Your grade is D!")
    elif 0 == score_number < 0.6:
        print("Your grade is F!")

#ASKING THE USER HIS SCORE:
score = input("Enter here your score that must be between 0.0 a 1.0: ")

#CALLING THE FUNCTING AND PRINTING THE GRADE:
calculation_score(score)