print("This program will count how many words are in the line text provided from the User and how many times it's repeated.")

#Variables
counts = dict ()
line = input("Text: ")

#Splitting 
words = line.split()
len_words = len(words)

#Counting:
for word in words:
    counts[word] = counts.get(word, 0) + 1

#Result
print("The numbers of words is:", len_words)
print("The repetition of wich word is:", counts)






