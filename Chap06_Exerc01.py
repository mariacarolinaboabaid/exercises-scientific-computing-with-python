#PRITING THE WORD GIVEN BY THE USER BACKWARD:

#GETTING THE WORD FROM THE USER:
user_word = input("Insert a word: ")

#PRITING:
x = len(user_word)
while x > 0:
    print(user_word[x - 1])
    x = x - 1
