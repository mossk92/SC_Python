print("FUNCTIONS CLASSWORK")
print("-----------------------------------------------")

print("Simple Function:")

def create_greeting(name):
        #this is the name of the function that you can call later. Inside the brackets is a variable to define later
    greeting = f"Hello {name}"
    return greeting
        #return is similar to print however will not actually show anything on the screen unless the function is called

print(create_greeting("Chilli"))
print(create_greeting("Ivy"))
print(create_greeting("Remus"))

print()
print("Function to take integer and multiply by 3:")
print("      Option 1: Ask for input")

def ask_integer():
        #this option asks for an input and multiplies that input
    integer = int(input("How old are you? "))
    return integer

print(ask_integer()*3)

print("      Option 2: Print Input")

def time_three(num):
    return num*3

print(time_three(10))

print("      Option 3: ")

print("      Option 4: ")

print()
print("Function to Convert:")

def convert_cm_to_inch(length_cm):
    length_in_inch = length_cm / 2.54
    return length_in_inch

print(convert_cm_to_inch(20))

def convert_inch_to_cm(length_in):
    length_in_cm = length_in * 2.54
    return length_in_cm

print(convert_inch_to_cm(7.87))

print()
print("Add Function:")

def add(a,b):
    return a+b

print(add(2,3))

print()
print("Mean Function:")

def mean(a,b):
    return (a + b) / 2

print(mean(5,15))

print()
print("EXERCISES")
print("-----------------------------------------------")

print("Q1: Write a function that take a temperature in f and return the temp in c")

def temp_in_cel(temp_in_f):
    temp_in_cel = (temp_in_f - 32) * (5/9)
    return temp_in_cel

print(temp_in_cel(32))

print()
print("Q2: Write function that accepts one parameter (integer) and return Tree when it is odd or False when even")

def is_odd(num):
    if num % 2 == 0: 
            # % = modulo which looks for remainder when divided (essentially decimal)
            # If there is no remainder when divided by 2, it means the number is even
        return False
    else:
        return True

print(is_odd(2))

print()
print("Q3: Write a function that reutrn the mean of a list of numbers")

def mean(num_list):
    return sum(num_list) / len(num_list)

print(mean([4,3,2,6]))

print(mean([10,5,6]))

print()
print("Q4: Write a function that takes two parameters; unit price and # of units and returns the total cost as a string")

def total_cost(price,quantity):
    return price * quantity

print(f'${total_cost(4.25,3)}')

print()
print('########################################################')
print()