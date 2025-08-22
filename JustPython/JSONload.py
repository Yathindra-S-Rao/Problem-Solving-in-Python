import json

data = []
users = int(input("Enter number of users: "))

for i in range(users):
    usr = dict()
    usr["id"] = input("Enter user id:")
    usr["name"] = input("Enter username:")
    data.append(usr)

print(json.dumps(data, indent = 2))