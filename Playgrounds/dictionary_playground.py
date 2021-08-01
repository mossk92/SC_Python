#Dictionary
    # Rules: keys must be unique and be only be immutable
    #Elements are key:value pairs
    # Immutable data types -> strings, Integer, Float, Boolean, List
    # Values do not need to be unique, they can be anything
    # Dictionaries are unordered

students_dict = {"Angela":1,"Jen":2,"Bel":3}
    # uses curly brackets
    #key (ie Angela) and then value after a colon
    #each entry is seperated with coma

print(students_dict)

print(students_dict["Angela"])

#Add to the dictionery
students_dict["Asli"] = 4
print(students_dict)

students_dict["Jen"] = 10
    #overwrights value with this if the key is alreayd there
print(students_dict)

del students_dict["Asli"]
    #deletes the whole elements
print(students_dict)

print(students_dict.keys())
    #prints all the keys within the dictionery

print(students_dict.items())
    #prints all the elements within the dictionery

#Iteration

for key in students_dict:
    print(key)
        #prints each key on a seperate line

for key in students_dict:
    print(key, students_dict[key])
        #prints each key with the value and no formatting

for key,value in students_dict.items():
        #same as above just different way of doing it
    print(key, value)

teacher_dict={"Asli":1,"Carlie":2,"Randal":3}

print(teacher_dict.get("Randal"))
    #provides the value of the key given

print(teacher_dict.get("Bel"))
    #will return 'None', as Bel isn't in the dict

print(teacher_dict.get("Bel",0))
    #essentially if then statement. Look for Bel, if you don't find it return 0
    # 0 can be a string, int or float