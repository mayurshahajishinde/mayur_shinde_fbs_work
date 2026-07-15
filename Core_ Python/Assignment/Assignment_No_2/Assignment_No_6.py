#write a program to calculatate total salary of employee based on basic da=10% of basic , ta=12% of basic hra=15% 0f base.

basic = float(input('Enter Basic Salary:'))
da = basic*10/100
ta = basic*12/100
hra = basic*15/100
total_salary = basic+ da +ta + hra
print(f'Total salary of employee is={total_salary}')