import requests
import json

BASE_URL = 'https://gorest.co.in/public/v2/users'


def get_users():
    return requests.get(BASE_URL)


with open('response.txt', 'w') as file:
    data = json.dumps(get_users().json(), indent=4)
    file.write(str(data))
