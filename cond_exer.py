#Q1) Roars Moth Catching
print("Time to Catch?")

moths_in_house = False
if moths_in_house:
    print("      Get the moths!")
else:
    print("      No threats detected.")

print()
print()
#Q2) Help Needed
print("Time to catch with help")

moths_in_house = False
mitch_is_home = True
if moths_in_house and mitch_is_home:
    print("      Hoooman! Help me get the moths!")
elif moths_in_house:
    print("      Meoooooooooooow! Hissssss!")
elif mitch_is_home:
    print("      Climb on Mitch.")
else:
    print("      No threats detected.")

print()
print()
#Q3) Red Light Cameras
print("Red Light Cameras")

light_colour = "Green"
car_detected = True
if light_colour == "Red" and car_detected:
    print("      Flash!")
else:
    print("      Do nothing.")

print()
print()

#Q4) Rollercoaster Height
print("Rollercoaster")

height = input("      What is your height in cm? ")

if int(height) >= 120:
    print("         Hop on!")
else:
    print("         Sorry, not today :(")

print()
print()

#Q5) Log In Details
print("Log In")

user = "fleur"
code = "password123"

username = input("      Please enter your username: ")
password = input("      Please enter your password: ")

if (username == user) and (password == code):
    print("         Correct!")
elif (username == user):
    print("         Check your Password")
elif (password == code):
    print("         Check your username")
else:
    print("         Incorrect!")

print()
print()

#Q6) Email Validation
print("Email Validation")

email = input("      Please enter your email: ")

if ("@" in email) and ("." in email):
    print("         Valid Email Address")
else:
    print("         Invalid Email Address")

print()
print()