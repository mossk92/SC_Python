print("CLASSWORK")
print("-----------------------------------------------")

print("Reading CSV:")
import csv
from typing import Collection, Counter

with open("data/dogs_are_awesome.txt", mode = "r", encoding = "utf-8") as csv_file:
        #mode default position is r, so this is not always required. r = read, w = write
        #encoding default position is utf-8 so this is not always required
        #csv_file is arbitrary name, could be anything
    csv_reader = csv.reader(csv_file, delimiter=",")
            #create the reader object
            #goes through file line by line and creates a list per line
            #delimiter default position is "," but can be changed when needed
    for line in csv_reader:
        print(line)

print()
print("Amending CSV:")
import csv

katie_said = []

with open("data/dogs_are_awesome.txt", mode = "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        print(line)
        katie_said.append(line)
            #adds the data from the csv into the 'katie said' file

print(katie_said)

print()
print("Creating CSV:")
import csv

with open("data/katie_says.txt", mode = "w", newline="") as csv_file:
        #if this text file does not exist, it will add it
        #if this text file does exist, it will amend it
        #newline helps with handling of data across any operating system
    csv_writer = csv.writer(csv_file)
            #creates the writer object
    for item in katie_said:
        csv_writer.writerow(item) 
                #strings or lists
                #does not print anything but will create a new file

print()
print("Reading Example:")

import csv

population = []

with open("data/2016_pilbara.csv", mode="r", encoding="utf-8") as csv_file: 
        #if file is not in same folder - need to express the full file structure required
    csv_reader = csv.reader(csv_file) 
    for line in csv_reader:
        population.append(line)

print(population)

print()
print("Amending Example:")

for age_group in population:
    print(f"{age_group[0]} {age_group[1]}")
            #removes list formatting and arranges columns as needed

print()
print("Creating Example:")

with open("data/population.csv", mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
            #creates new file, no data inside

print()
print('########################################################')
print()

print("EXERCISES")
print("-----------------------------------------------")

print("Q1: Read and Output Colour data")

with open("data/colours_20_simple.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for column in csv_reader:
        print(f'{column[0]} {column[1]} {column[2]}')

print()
print("Q2: Amend order of Colour data")

with open("data/colours_20_simple.csv") as csv_file_simple:
    csv_reader = csv.reader(csv_file_simple)
    next(csv_reader)
            #this takes the first row and discards it
    for column in csv_reader:
        print(f'{column[2]}, Hex: {column[1]}, RGB: {column[0]}')

print()
print("Q3: Amending and Remvoing Data")

with open("data/colours_20.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for column in csv_reader:
        print(f'{column[4]}, Hex: {column[2]}, RGB: {column[1]}')

print()
print("Q4: Count Colours from Column")

countRed = 0
countGreen = 0
countBlue = 0
countYellow = 0

with open("data/colours_20.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for column in csv_reader:
        if "red" in column[4]:
            countRed += 1
        if "green" in column[4]:
            countGreen += 1
        if "blue" in column[4]:
            countBlue += 1
        if "yellow" in column[4]:
            countYellow += 1
        
print(f'Red: {countRed}')
print(f'Green: {countGreen}')
print(f'Blue: {countBlue}')
print(f'Yellow: {countYellow}')


print()
print("Q5: Finding Min and Max Values")
import csv

with open("data/galaxies.csv") as csv_gal:
    csv_reader = csv.reader(csv_gal)
    for sheet in csv_reader:
        print(sheet)

def minVel():
    return min(sheet[2])

    # minVel, maxVel = [],[]
    # for column in csv_reader:
    #     minVel = min(column[2))
    #     maxVel = max(column[2])

print(f'minGal has the min velocity of {minVel()}')
# print(f'maxGal has the max velocity of {maxVel}')

print()
print('########################################################')
print()