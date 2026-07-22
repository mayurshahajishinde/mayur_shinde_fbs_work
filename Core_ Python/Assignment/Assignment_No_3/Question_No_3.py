# write a program to check triangle is valid or invalid triangle using angles.

num1 = int(input('Enter first angle:'))
num2 = int(input('Enter second angle:'))
num3 = int(input('Enter third angle:'))
if num1 + num2+ num3 ==180:
        print('Valid Triangle')
else:
         print('Invalid Triangle')