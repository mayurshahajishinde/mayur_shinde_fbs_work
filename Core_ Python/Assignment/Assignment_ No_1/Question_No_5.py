#write a program to enter P.,T,R and calculate compond intrest.

P = int (input('Enter principal amount:'))
T = int (input('Enter time in year:'))
R = float(input('Enter rate of intrest:'))
ks =P*(1+R/100)**T-P
print('compond intrest is:',ks)