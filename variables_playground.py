print("VARIABLES CLASSWORK")
print("-----------------------------------------------")

print("String:")
day = "Saturday"
month = "July"
    # Strings are words or phrases
    # They are contained within "" or ''
message = f"Today is {day}, {month}"

print(message)
print(type(day))

print()
print("Integer:")

apples = 5
banana = 8
    # Integers are whole numbers
    # They are written as is with no formatting
fruits = apples + banana

print(fruits)
print(type(fruits))

print()
print("Float:")

height = 1.70
weight = 999.9
    #Floats are decimal numbers
    #They are shown wth a decimal place
calculation = weight - height
print(calculation)
print(type(calculation))

calculation = height + banana
print(calculation)

print()
print("Add Integers:")

#Run distance in m
run1_dist = 1400
run2_dist = 1800

total_dist = run1_dist + run2_dist

print(total_dist)

print()
print("Add Floats:")

#Run Distance in km
run3_dist = 1.7
run4_dist = 1.35

total_dist = run3_dist + run4_dist

print(total_dist)

print()
print("Division:")

m_dist = run1_dist / run2_dist
print(m_dist)
print(run1_dist / 1000)
print(run3_dist * 1000)
print(type(m_dist))
    #Result of division will always by a float regardless of if answer is whole or not

print()
print("Comparing different types:")

var1 = "banana"
var2 = 5
var3 = "3"
var4 = 10

#str + int
#print(var1 + var2)
    #will fail as python cannot cross type

#use int as string
print(var1 + str(var2))  
print(var1 + var3)  

#use string as int
print(var2 + int(var3))

#multiply str by int
print(var1 * var2)
    #duplicates string by the amount of the integer

#int to float
print(float(var2))
print(type(var2))

#Divisions are float regardless of inputs
calculation = var4 / var2
print(type(var4))
print(type(var2))
print(calculation)
print(type(calculation))

print()

print()
print("EXERCISES")
print("-----------------------------------------------")

print("Q1: ")



print()
print("Q2: ")



print()
print("Q3: ")



print()
print("Q4: ")



print()
print('########################################################')
print()