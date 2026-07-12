#Find the area of circumference of circle.

import math
radius = float(input('Enter the radius of the circle:'))
area = math.pi * radius**2
circumference = 2 * math.pi + radius
print('Area of circle is:',area)
print('Circumference of the circle is:',circumference)
