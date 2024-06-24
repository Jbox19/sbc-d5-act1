#stack = FILO (First In Last Out) or (Last in First Out)
#queue = FIFO (First In First Out) or (Last in Last Out)
val1 = input("Input value: ") 
val2 = input("Input value: ") 
val3 = input("Input value: ")
val = f"{val1} {val2} {val3}"
dis = input('Input "display" to view or press enter to ignore: ').capitalize()
if dis == "Display":
    print(val) 
list = [val1, val2, val3]
while True:
    office = input("Naa, Wala, Add ? ").capitalize()
    print(office)

    if office == "Naa":          #idea of stack
        list.pop(0)
        print(list)
        if list == []:
            print("List is empty")
            break
    elif office == "Wala":       #idea of queue
        list.pop(-1)
        print(list)
        if list == []:
            print("List is empty")
            break
    elif office == "Add":
        add = input("add value: ")
        list.append(add)
        print(list)
    else:
        print("Laagan si boss")
        break