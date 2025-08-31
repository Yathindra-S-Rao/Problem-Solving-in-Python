items = list()


while True:
    item = input("Add item: ")
    if item == "-1":
        break
    else:
        items.append(item)
        

print("Iteams list :", items)