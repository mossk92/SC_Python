#Q1) Ask user for number and print times table for that number
user_input = input("Please enter a number: ")

for number in range(int(user_input)):
    print(f"{user_input} * {number+1} = {int(user_input)*(number+1)}")