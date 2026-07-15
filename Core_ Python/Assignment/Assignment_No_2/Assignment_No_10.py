# write a program to reverse three digit numbers.
num = int(input('Enter number:'))
d1=num %10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

reverse= (d1*100) + (d2*10) + d3
print(f'Reverse of three didit number is={reverse}')