#       input format xxxxGxx$xxT
#       If $ (money) is just next to T (Thief), program should print 'Alarm' or else 'Quiet'

security = input("Enter the floor layout by entering Guard, Thief and Money's position:")
flow = ""

for i in security:
    if i == "x":
        pass
    elif i == "T" or i=="$" or i=="G":
        flow += i
        
if "T" in flow:
    if abs(flow.index("$") - flow.index("T")) >= 2:
        print("Quiet")
    else:
        print("Alarm")
else:
    print("There is no theif in the floor. Your money is safe")
