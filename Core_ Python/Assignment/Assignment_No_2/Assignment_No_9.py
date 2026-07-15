# write a program to swap two numbers without using  third variable.

x = int(input('Enter fist number:'))
y = int(input('Enter second number:'))
print(f'Before swapping: x={x}, y ={y}')

x,y=y,x

print(f'After swapping:= x={x}, y={y}')