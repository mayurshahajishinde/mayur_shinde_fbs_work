#find the sum of three digit numbers.

num = int(input('Enter number:'))
temp =  num

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10
num=num//10

sum_digit= d1 +d2 +d3
print(f'The total sum of three digit is={sum_digit}')