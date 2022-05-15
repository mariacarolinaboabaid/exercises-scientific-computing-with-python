#THIS PROGRAM WILL COUNT THE CHARACTERS INSIDE A WORD BOTH CHOSEN BY THE USER:

#DEFINING THE FUNCTION:
def counting_words(world, character):
    count = 0
    for letter in world:
        if letter == character:
            count = count + 1
    print(count)

#GETTING THE CHARACTER AND WORD FROM THE USER:
user_string = input("Enter a world: ")
user_character = input("Enter a character: ")

#RESULT:
counting_words(user_string, user_character)