#write a program to accpect an integer amount from user and tell minimum number of notes needed to reprsenting that amount.

amount = int(input('Enter amount:'))
n500=amount//500
amount=amount%500

n200=amount//200
amount=amount%200

n100=amount//100
amount==amount%10

n50=amount//50
amount=-amount%50

n20=amount//20
amount=amount%20

n10=amount//10
amount=amount%10
print(f'500 notes={n500}.')
print(f'200 notes={n200}.')
print(f'100 notes={n100}.')
print(f'50 notes={n50}.')
print(f'20 notes={n20}.')
print(f'10 notes={n10}.')
