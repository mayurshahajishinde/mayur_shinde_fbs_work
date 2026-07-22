# Ticket amount for five person.

age1 = int(input('Enter the first age:'))
tprice1 = float(input('Enter the first tprice:'))
totalprice=0
if (age1 < 12):
    totalprice = totalprice +(tprice1 * 0.30)
elif (age1< 59):
    totalprice = totalprice +(tprice1 * 0.50)
else:
    totalprice = totalprice + tprice1

age2 = int(input('Enter the second age:'))
tprice2 = float(input('Enter the second tprice:'))
if (age2 < 12):
    totalprice = totalprice +(tprice2 * 0.30)
elif (age2< 59):
    totalprice = totalprice +(tprice2 * 0.50)
else:
    totalprice = totalprice + tprice2


age3 = int(input('Enter the third age:'))
tprice3 = float(input('Enter the third tprice:'))
if (age3 < 12):
    totalprice = totalprice +(tprice3 * 0.30)
elif (age3< 59):
    totalprice = totalprice +(tprice3 * 0.50)
else:
    totalprice = totalprice + tprice3

age4 = int(input('Enter the fourth age:'))
tprice4 = float(input('Enter the fourth tprice:'))
if (age4 < 12):
    totalprice = totalprice +(tprice4 * 0.30)
elif (age4< 59):
    totalprice = totalprice +(tprice4 * 0.50)
else:
    totalprice = totalprice + tprice4


age5 = int(input('Enter the fifth age:'))
tprice5 = float(input('Enter the fifth tprice:'))
if (age5 < 12):
    totalprice = totalprice +(tprice5 * 0.30)
elif (age5< 59):
    totalprice = totalprice +(tprice5 * 0.50)
else:
    totalprice = totalprice + tprice5

print(totalprice)

