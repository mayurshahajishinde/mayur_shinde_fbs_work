#Write a program to prompt user to enter userid and# password. If Id and  password is incorrect give him chance to re-enter the credentials.
#  Let him try 3  times. After that program to terminate
  
user = 'mayur'
pass1 = '@4563'

for i in range(4):
    userid = input('Enter userid:')
    password = input('Enter password:')

    if userid == user and password == pass1:
        print('Login successfully.')
        break
    else:
        remaining = 3-i
        print('Incorrect credential remaning attempts:',remaining)

else:
    print('Program terminate becasuse of too many attempts.')

