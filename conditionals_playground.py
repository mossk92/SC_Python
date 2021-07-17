print("CLASSWORK")
print("-----------------------------------------------")

print("Booleans:")
    #True or false statements

is_raining = False
is_cold = True

print(type(is_raining))
print(type(is_cold))

print()
print("Operators:")

print(is_raining and is_cold)
    #will print true is both variables are true
print(is_raining or is_cold)
    #will print true if either variable is true
print(not is_raining)
    #will print the opposite of the variable

print()
print("Statements:")

print(5 < 3)
    #will print true if first variable is less then second
print(5 > 3)
    #will print true if first variable is greater then second
print(10 >= 10)
    #will print true if first variable is greater then or equal to second
print(4 <= 10)
    #will print true if first variable is less then or equal to second
print(5 == 5)
    #checks if the values are the same
print(5 != 5)
    #checks if the values are not equal
print("Katie" != "katie")
    #text is case sensitive when make checks so above is not equal

print()
print("If Statements:")

temperature = 16
wind_chill = 3
raining = False

if temperature - wind_chill < 16:
    print("Take a jumper.")
elif temperature - wind_chill > 30:
    print("Euck, it's hot today, stay home")
else:
    print("Wow, what a lovely day")

print()
print("Nested If Statements:")

if temperature - wind_chill < 18 and raining:
    print("Just stay home")
else:
    if raining:
        print("You'll need an umbrella today")
    if temperature-wind_chill < 14:
        print("You'll need a jumper")

print()
print('########################################################')
print()

print("EXERCISES")
print("-----------------------------------------------")

print("Q1: Moth Catching:")

moths_in_house = False

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")

print()
print("Q2: Moth Catching with Help")

moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif moths_in_house:
    print("Meoooooooooooow! Hissssss!")
elif mitch_is_home:
    print("Climb on Mitch.")
else:
    print("No threats detected.")

print()
print("Q3: Red Light Cameras")

light_colour = "Green"
car_detected = True

if light_colour == "Red" and car_detected:
    print("Flash!")
else:
    print("Do nothing.")

print()
print("Q4: Rollercoaster Height")

height = input("What is your height in cm? ")

if int(height) >= 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")

print()
print("Q5: Log In Details")

user = "fleur"
code = "password123"
username = input("Please enter your username: ")
password = input("Please enter your password: ")

if (username == user) and (password == code):
    print("Correct!")
elif (username == user):
    print("Check your Password")
elif (password == code):
    print("Check your username")
else:
    print("Incorrect!")

print()
print("Q6: Email Validation")

email = input("      Please enter your email: ")

if ("@" in email) and ("." in email):
    print("         Valid Email Address")
else:
    print("         Invalid Email Address")

print()
print('########################################################')
print()