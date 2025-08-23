import json

# JSON Data
json_data = '''
[
  {
    "id": "0001",
    "name": "Yathindra",
    "roles": ["manual testing", "automation"]
  },
  {
    "id": "0002",
    "name": "Atul",
    "roles": ["developer", "python", "selenium"]
  },
  {
    "id": "0003",
    "name": "Priya",
    "roles": ["QA lead", "robot framework", "API testing"]
  },
  {
    "id": "0004",
    "name": "Rahul",
    "roles": ["DevOps", "AWS", "Docker"]
  }
]
'''

# Load JSON string into Python list of dicts
data = json.loads(json_data)

# Find user with ID = 0003
for user in data:
    if user["id"] == "0002":
        print(f"Name: {user['name']}")
        print(f"Roles: {user['roles']}")
        break