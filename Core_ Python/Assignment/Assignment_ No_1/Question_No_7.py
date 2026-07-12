#write a program to find the roots of a Quadratic Equation.
import cmath

a=int(input('Enter coefficient a:'))
b=int(input('Enter coefficient b:'))
c=int(input('Enter coefficient c:'))

#calculate the discriminate
d=(b**2)-(4*a*c)

#Find the two roots
root1=(-b- cmath.sqrt(d)) / (2*a)
root2=(-b+ cmath.sqrt(d)) / (2*a)
print(f'The root are{0} and {1}'.format( root1, root2 ))


