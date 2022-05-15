#THIS PROGRAM WILL SHOW THE SUM, AVERAGE AND THE TOTAL OF THE NUMBERS THAT THE USER PROVIDES UNTIL HE ENTERS "DONE!"

#DECLARING VARIABLES:
user_number_list = list ()

#ASKING THE USER A NUMBER:
while True:
    question = input("Enter a number or 'Done!': ")
    if question == "Done!":
        break
#ADDING THE USER NUMBER TO THE USER_NUMBER_LIST:
    else:
        try:
            question = float(question)
            user_number_list.append(question)
#IF THE USER DOES NOT ENTER NUMBER:
        except:
             print("Bad data!")
#PRITING THE RESULT:
print(sum(user_number_list), len(user_number_list), (sum(user_number_list)/len(user_number_list)))

    

