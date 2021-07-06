#String
day = "Saturday"
month = "July"
message = f"Today is {day}, {month}"

print(message)
print(type(day))

#Integer
apples = 5
banana = 8
fruits = apples + banana

print(fruits)
print(type(fruits))

#Float
height = 1.70
weight = 999.9
calculation = weight - height
print(calculation)
print(type(calculation))

calculation = height + banana
print(calculation)

#Integers
#Run Distance in m
run1_dist = 1400
run2_dist = 1800

#Addition
total_dist = run1_dist + run2_dist

print(total_dist)

#Floats
#Run Distance in km
run3_dist = 1.7
run4_dist = 1.35

#Addition
total_dist = run3_dist + run4_dist

print(total_dist)

#Division 
m_dist = run1_dist / run2_dist
print(m_dist)
print(run1_dist / 1000)
print(run3_dist * 1000)
print(type(m_dist))

#Test Case
goal_dist = 3000
run1_left = goal_dist - run1_dist
print(run1_left)

#Combining different types
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