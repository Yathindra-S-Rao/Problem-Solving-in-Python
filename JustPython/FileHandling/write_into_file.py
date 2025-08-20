import requests

BASE_URL = 'https://gorest.co.in/public/v2/users'


def get_users():
    return requests.get(BASE_URL)


with open('response.txt', 'w') as file:
    file.write(str(get_users().json()))


