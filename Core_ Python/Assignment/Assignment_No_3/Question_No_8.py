 #CAPTCHA program

import random

userid = input("Enter UserId: ")
Password = input("Enter password: ")

if userid == 'mayur' and Password == '123':
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    user = int(input("Enter Captcha: "))

    if user == captcha:
        print("Login Successful")
    else:
        print("Captcha Incorrect")
else:
    print("Invalid UserId or Password")