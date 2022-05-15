print("This programm will read the numbers given from the User untill he enters 'done', after that is gonna show the total of the sum and iterations, and the average of the numbers")

num_iterations = 0
total_sum = 0.0

while True:
    number_user = input("Enter a number untill you are done: ")
    if number_user == "done":
        break
    try:
        number = float(number_user)
        num_iterations = num_iterations + 1
        total_sum = total_sum + number
    except:
        print("Invalid input")
        continue


print("Result: ", total_sum, num_iterations, total_sum/num_iterations)
