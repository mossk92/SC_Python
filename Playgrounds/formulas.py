#syntax
len("asli")
range(1,2)

def ask_name():
    name = input("What's you name? ")
    return name  #stops on this function

asli_name = ask_name()
print(asli_name)

def create_greeting(name):
    greeting = f"Hello {name}"
    return greeting

print(create_greeting("Chilli"))

def convert_cm_to_inch(length_cm):
    length_in_inch = length_cm / 2.54
    return length_in_inch

print(convert_cm_to_inch(20))

def add(a,b):
    #result = a+b
    #return result
    #return a+b

print(add(2,3))