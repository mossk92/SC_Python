print("")
print("CLASS WORK")
#Understanding Lists

dog_wishlist = ["igloo","chicken","donut toy","cardboard box"]

#indexing
print(len(dog_wishlist)) #prints the number of items in the list
print(dog_wishlist[3]) #prints the 3th index - which is actually the 4th item
print(dog_wishlist[0]) #prints the 0 index - which is actually 1st item
print(dog_wishlist[-1]) #prints last item in list
print(dog_wishlist[0:2]) #prints from the 0 index, and included items until the next index (not inclusive) - so 1st item to 2nd item
print(dog_wishlist[1:3]) #prints 2nd item to 3rd item

#Add to a list
dog_wishlist[1] = "carrot" #changes the first index (2nd item) to carrot
print(dog_wishlist)

dog_wishlist.append("dig mat") #add to end - use append for single additions
dog_wishlist.extend(["kong","tennis ball","crocodile toy"]) #add to end - use extend for multiple additions
dog_wishlist.insert(1,"peanut butter") #add item before index - add peanut butter before 2nd item
print(dog_wishlist)

#remove from list
dog_wishlist.pop() #removes the last item from the list
dog_wishlist.pop(2) #removes the second index - 3rd item
dog_wishlist.remove("kong") #removes a specified item
print(dog_wishlist)

#logic with lists
if "tennis ball" in dog_wishlist:
    print("Chilli would like a tennis ball")
else:
    print("Chilli doesn't feel like playing fetch")

if len(dog_wishlist) > 8:
    print("Chilli wants a lot of stuff")

#Sub lists
dog_categories = [
    ["igloo"], #bed
    ["donut toy","tennis ball","crocodile toy"], #toys
    ["chicken","peanut butter"], #treats
    ["cardboard box","kong","dig mat"] #activity based toys
]

print(dog_categories[2]) #prints the entire second index, even if a list - so the 3rd items
print(dog_categories[2][1]) #prints from the second index and the first indexin it - so the 3rd item and 2nd item

print("")
print("")
print("EXERCISES")
#Q1) ??
print("Q1 ??:")

print()