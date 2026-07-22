# check whether three digit is pallindrome or not pallindrome.

num = int(input('Enter number you want:'))
tem = num
rev = 0
while(num > 0):
    d = num % 10
    num = num // 10
    rev = rev * 10 + d
    print(d)

if( tem == rev):
    print('Pallindrome.')
else:
    print('Not pllindrome.')
