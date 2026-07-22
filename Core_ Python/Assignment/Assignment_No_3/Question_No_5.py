# check triangle type.

num1 = int(input('Enter First Triangle:'))
num2 = int(input('Enter Second Triangle:'))
num3 = int(input('Enter Third Triangle:'))
if num1 == num2 == num3:
 print('Equilateral triangle.')
elif num1 == num2 or num2 == num3 or num1 == num3:
 print('Isosceles Triangle.')
else:
 print('Scalene Triangle.')
 