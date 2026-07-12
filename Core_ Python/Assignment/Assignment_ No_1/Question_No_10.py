#write a program to calculate area of an equililateral triangle.

import cmath
side = float(input('Enter the length of side of the quililateral triangle: '))
area = (cmath.sqrt(3)/(4)) * side**2
print('Area of the quililaterai triangle is:',area)