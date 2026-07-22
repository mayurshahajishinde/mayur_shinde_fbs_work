# Marriage eligibility

gender = (input('Enter gender(m/f):'))
age = int(input('Enter age:'))
if(gender =='f'):
    if(age >= 18):
      print('Girl is eligable for marriage.')
    else:
        print('Girl is not eligibal for marriage.')
else:
 if(gender=='m'):
   if(age >= 21):
      print('Boy is  eligibal for marriage.')
   else:
      print('Boy  not eligibal for marriage.')

