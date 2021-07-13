#loops - repetitive tasks
#loop - for loops, while loops
    # for num in range(5): # cycles through numbers in that range
        # print(num)

#Loop to print number 0 to 100 (inclusive)
    # for num1 in range(101):
        # print(num1)

#Loop to print numbers 0 to 100 (in 5 intevals)
    # for num2 in range(0,101,5):
        # print(num2)

# Cumulative results
letters = ["a","b","c","d"]

result = ""  #initialise a str

    # for letter in letters:
        # result = result + letter
        # print(result) #can take this outside of for to only print last line

# 
chilli_wishlist = ["igloo","chicken","donut toy","cardboard box"]

    # for item in range(len(chilli_wishlist)): 
        # print(chilli_wishlist[item]) #cycle through all elements (quicker to not use range though)

#Adapt for loop to print a message e.g. #Adapt tge for loop to print a message
    # for item in chilli_wishlist:
        # print(f"Chilli wants: {item}") #f format string needs curly brackets if referencing out

#Use a for loop to print each item in a list
names = ["Brooke","Carlie","Katie","Stacey"]

    # for name in range(len(names)):
    #     print(name)

#Nested Loops
    # mila_wishlist = [
    #     ["igloo"],
    #     ["donut toy","tennis ball","crocodile toy"], 
    #     ["chicken","peanut butter"]
    #     ["cardboard box","kong","dig mat"]
    # ]

    # for category in mila_wishlist:
    #     for item in category:
    #         print(item)

#While Loops - don't know how long they 
    # count = 10

    # while count <= 10:
    #     print(counter)
    #     count = count + 1

#Ask the user to continually enter names until a blank string is entered
enter_name = "Katie"

while enter_name != "":
    enter_name = input("Guess a name: ")

#Ask the user continually enter password until a password that you sethas been given
user_input=""
password="fruitloops"

while password != user_input:
    user_input = input("Enter Password: ")