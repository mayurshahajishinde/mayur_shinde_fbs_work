#write a program to enter P,T,R and calculate simple intrest.

P = float(input('Enter principle amount:'))
T = float(input('Enter time in year:'))
R = float(input('Enter rate of intrest'))

ms=(P*R*T)/100
print('simple intrest is:',ms)