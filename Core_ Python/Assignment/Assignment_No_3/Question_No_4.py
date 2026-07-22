# check whether triangle is valid or invalid using sides.

num1 = int(input('Enter First Side:'))
num2 = int(input('Enter Second Side:'))
num3 = int(input('Enter Third Side:'))
if(num1 + num2 > num3) and (num1 + num3  > num2) and (num2 + num3 > num1):
    print('Valid triangle.')
else:
    print('Invalid triangle.')