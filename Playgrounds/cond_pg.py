#boolean (ture or false statements)
is_raining = False
is_cold = True

#operators
print(is_raining and is_cold)
print(is_raining or is_cold)
print(not is_raining)

print (is_raining and not is_cold)

#Guessing Game
print(is_raining) #F
print(not is_raining) #T
print(is_raining or is_cold) #T
print(is_raining and not is_cold) #F
print(is_raining or not is_cold) #F
print(not is_raining and not is_cold) #F

#Statements
print(5 < 3)
print(5 > 3)
print(10 >= 10)
print(4 >=10)
print(5 == 5) # checks if the values are the same
print(5 != 5) # check if the values are not the same

print(5.1 > 2.4)
print("Asli" != "asli") #if text is not completely the same, then it will be false (such as capitals)

#test
temperature = 16
print(temperature < 18)
wind_chill = 3
print(wind_chill > 4)

#If Statements
temperature = 16
wind_chill = 3
raining = False

if temperature - wind_chill < 16:
    print("Take a jumper.")
elif: temperature - wind_chill > 30:
    print("Euck, it's hot today, stay home")
else:
    print("Wow, what a lovely day")

#Nested if Statements
if temperature - wind_chill < 16 and raining:
    print("Just stay home")
else:
    if raining:
        print("You'll need an umbrella today")
    if temperature- wind_chill < 13:
        print("You'll need a jumper")