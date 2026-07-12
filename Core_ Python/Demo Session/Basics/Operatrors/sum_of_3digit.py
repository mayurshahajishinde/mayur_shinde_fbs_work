#find sum of three digit

num=379 

d1=num%10
num=num//10

d2=num%10
num=num//10

d3=num%10           #o/p 19
num=num//10
print(num)

sum=d1+d2+d3
print(sum)