print("DICTIONARY CLASSWORK")
print("-----------------------------------------------")

    # Rules: keys must be unique and be only be immutable
    #Elements are key:value pairs
    # Immutable data types -> strings, Integer, Float, Boolean, List
    # Values do not need to be unique, they can be anything
    # Dictionaries are unordered

print()
print("Example 1:")

students_dict = {"Angela":1,"Jen":2,"Bel":3}
    # uses curly brackets
    #key (ie Angela) and then value after a colon
    #each entry is seperated with coma

print(students_dict)
    #this will print the whole dictionary

print(students_dict["Angela"])   
    #this will print the value for the key given

print(students_dict.keys())
    #prints all the keys within the dictionery

print(students_dict.items())
    #prints all the elements (keys : Value) within the dictionery

students_dict["Asli"] = 4
    #Add to the dictionery
print(students_dict)

students_dict["Jen"] = 10
    #overwrights value with this if the key is already there
print(students_dict)

del students_dict["Asli"]
    #deletes the whole elements
print(students_dict)

for key in students_dict:
   print(key)
        #prints each key on a seperate line

for key in students_dict:
    print(key, students_dict[key])
        #prints each key with the value and no formatting

for key,value in students_dict.items():   
    print(key, value)
        #same as above just different way of doing it



print()
print("Example 2:")

teacher_dict={"Asli":1,"Carlie":2,"Randal":3}

print(teacher_dict.get("Randal"))
    #provides the value of the key given

print(teacher_dict.get("Bel"))
    #will return 'None', as Bel isn't in the dict

print(teacher_dict.get("Bel",0))
    #essentially if then statement. Look for Bel, if you don't find it return 0
    # 0 can be a string, int or float



print()
print("Example 3:")

groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}

print(groceries["Baby Spinach"])
    #look for a specific value

groceries["Avocadoes"] = 1.0
print(groceries)
    #Add a new item

groceries["Hot Chocolate"] = 2.70
print(groceries)
    #Change value of existing item

del groceries["Crackers"]
print(groceries)
    #remove item from dictionary

for item in groceries:
    print(f"{item}: ${groceries[item]}")
        #iterate over the dictionary

for item, price in groceries.items():
    print(f"{item}: ${price}")
        #another way to iterate over the dictionary

print()
print('########################################################')
print()

print("EXERCISES")
print("-----------------------------------------------")

print("Q1: Change Visual of dictionary ")

groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2,
}

for item in groceries:
    print(f'{quantity[item]} {item} @ ${groceries[item]} = {quantity[item] * groceries[item]:.1f}')
        #:.2f rounds to exact decimal placing

print()
print("Q2: Iterate over List and track number of occurrences")

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}

colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green",
]

for colour in colours:
    colour_counts[colour] += 1

print(colour_counts)

print()
print("Q3: Create dictionary where each key is a name and value is occurrences")

names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy", "Joy", "Katie", "Maddie", "Tash", "Nic", "Rachael", "Bec", "Bec", "Tabitha", "Teagen", "Viv", "Anna", "Catherine", "Catherine", "Debby", "Gab", "Megan", "Michelle", "Nic", "Roxy", "Samara", "Sasha", "Sophie", "Teagan" , "Viv",
]

names_dict = {}.fromkeys(names,0)

for name in names:
    names_dict[name] += 1

print(names_dict)

print()
print("Q4: Read colour data and save dictionary where key is hex code and value is english name")

import csv

colour_dict = {}

with open("data/colours_20_simple.csv", mode = "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next (csv_reader)
    for line in csv_reader:
        colour_dict[line[1]] = line[2]

print(colour_dict)

print()
print("Q5: Modify your Q4 to include english and RGB code")
import csv

colour_dict = {}

with open("data/colours_20_simple.csv", mode = "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next (csv_reader)
    for line in csv_reader:
        colour_dict[line[1]] = [line[0],line[2]]

print(colour_dict)

print()
print('########################################################')
print()