#example 1

list = ["apple", "banana", "strawberry", "mango", "melon"]  #mutable = can be change
tuple = ("1", "2", "3", "4")                                #immutable = cannot be change
print(list[1])      
print(tuple[1:])
list[4] = "orange"                                          #changing value of index 4 from melon to orange
print(list)

#example 2

list = [1, 2, 3, 4]
print(len(list))        #to show the length of the list
print(list[0])
list.append("5")        #add value in last 
print(list)
list.insert(5, "6")     #add value using index to add value in any place
print(list)
list.remove(3)          #removing value inside the list
print(list)
list.pop(0)             #remove value using its index
print(list)


#example 3

list = [3, 2, 4, 1]
list.sort()             #sort - ascending
print(list)
list.sort(reverse=True) #sort - descending
print(list)

list1 = []
list1.append("BUNI Jords")
print(list1)
list1.insert(0, "BUNI Javier")
print(list1)
list1.remove("BUNI Javier")
print(list1)
list1.pop(0)
print(list1)

#example 4 

dictionary = {"message": "Hello World", 
     "java": "No Thanks",
     "python": "Yes Please",
     "Multiple": [1, 2, 3, 4, 5]}
print(dictionary["message"])
print(dictionary["Multiple"][0])

data = [["Aljieo", "O", "Tolibas"]]
final = []
for d in data:
    label = {}
    label["firstname"] = d[0]
    label["initial"] = d[1]
    label["lastname"] = d[2]
    final.append(label)
print(final)

#stack = FILO (First In Last Out) or (Last in First Out)
#queue = FIFO (First In First Out) or (Last in Last Out)
