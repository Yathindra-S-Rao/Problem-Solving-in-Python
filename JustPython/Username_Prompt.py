#       Program to accept username and validate with the list of users

allowed_users  = {"Pam", "Jim"}

while True:
    user = input("Login >>>")

    if user in allowed_users:
        print("Access granted")
        break
    else:
        print("Access denied")
