print("")
print("CLASS WORK")
#Boolean Values
print("Boolean Values:")
    #This have a True or False answer (must be capitalised)

is_raining = False
is_cold = True

print(type(is_raining)) 
print(type(is_cold)) #these will give a type of 'bool'

#Not statements
print(is_raining) #will print false
print(not is_raining) #will print true

#And statements
print(is_raining and is_cold) #willl print False (as not both conditions are true)
print(not is_raining and is_cold) #will print True (as both conditions are true)

#Math functions
temperature = 16
print(temperature < 18) #will only print if it is less then 18)
wind_chill = 3
print (wind_chill > 4) #will only print if greater then 4)
print(temperature - wind_chill < 16) #will only print if temp - wind is less then 16

#Equal or not equal
name = "Hayley"
print(name == "Hayley") #prints if the values are the same
print(name != "Hayley") #prints if the values are different

name2 = "Holly"
print(name2 == "Hayley") 
print(name2 != "Hayley") 

#If statements
print("If Statements:")

if is_raining: #if true it will complete the intented request
    print("Take an umbrella.") #will not print anything

#If and else: 

if is_raining:
    print("Take an umbrella.") 
else: #if the above is not true, it will complete the intended request below 'else'
    print("Do not take an umbrella") #will print this

#If, elif, else

if temperature - wind_chill < 16: #if true it will print the intent and stop
    print("Take a jumper.")  #will print this
elif temperature - wind_chill > 30: #if above not true and this is true, it will print intent and stop
    print("Euck, it's hot today, stay home")
else: #if all statements above are not true then it will complete intent
    print ("Wow, what a lovely day!")

#Nested if statements (ifs in ifs)

if temperature - wind_chill < 16 and is_raining: #if this is true it will print intent and stop
    print("Just stay home.")
else: #if above are not true, it will print intent
    if is_raining: #will only print if true
        print("You'll need an umbrella today")
    if temperature - wind_chill < 16: #will onlly print if true (but will print regardless if above is true or not
        print ("You'll need a jumper today")

print("")
print("")
print("EXERCISES")
#Q1) Moth Catching
print("Q1 Moth Catching:")

moths_in_house = False

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected")

print()
#Q2) Moth Catching Together
print("Q2 Moth Catching Together:")

moths_in_house = True
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hooman! Help me get the moths!")
elif moths_in_house:
    print("Meooooooooow! Hisssss!")
elif mitch_is_home:
    print("Climb on Mitch")
else:
    print("No threats detected")

print()
#Q3) Red Light Camera
print("Q3 Red Light Camera:")

light_colour = "Red"
car_detected = False

if (light_colour == "Red") and car_detected:
    print("Flash!")
else:
    print("Do nothing")

print()

#Q4) Rollercoaster
print("Q4 Rollercoaster:")

user_height = input("What is your height? ")

if int(user_height) >= 120:
    print("Hop On!")
else:
    print("Sorry, not today :(")

print()

#Q5) Password Validation
print("Q5 Password Validation:")

username = "fleur"
password = "password123"

user_entry = input("What is your username? ")
user_password = input("What is your password? ")

if (username == user_entry) and (password == user_password):
    print("Correct")
elif (username == user_entry):
    print("Check your password")
elif (password == user_password):
    print("Check your username")
else:
    print("Incorrect!")

print()

#Q6) Email validation
print("Q6 Email Validation:")

user_email = input("What is your email? ")

if ("@" in user_email) and ("." in user_email):
    print("Valid email address")
else:
    print("Invalid email address")

print()