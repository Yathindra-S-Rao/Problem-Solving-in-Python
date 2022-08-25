#       Program to demonstrate the decorators

logged_in = False


def check_login(method):
    def login():
        mpin = input("Enter mPIN : ")
        if int(mpin) == 0000:
            True
            method()
        else:
            print("Invalid mpin!")

    return login()


@check_login
def home_page():
    print("This is Home page")
