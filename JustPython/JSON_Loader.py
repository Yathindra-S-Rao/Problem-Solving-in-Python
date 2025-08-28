emp_details = [{
    "id" : 1001,
    "name" : "Yathindra S",
},
{
    "id": 1002,
    "name": "Raveena K S"
},
{
    "id" : 1003,
    "name": "Annapurna",
    "data": ["Kolige", "Shivamogga"]
}

]

import json

json_data = json.dumps(emp_details, indent=2)

print(json_data, type(json_data))
pydata = json.loads(json_data)
for each in pydata:
    if each["id"]==1003:
        print(each["data"])