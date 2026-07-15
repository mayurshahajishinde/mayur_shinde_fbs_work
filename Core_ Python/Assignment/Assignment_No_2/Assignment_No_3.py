#convert distant into feetband inches into meter and centimeters.

feet = int(input('Enter feet:'))
inches = int(input('Enter inches:'))

total_inches = (feet *12) + inches

meter = total_inches * 0.0254
centemeter = meter * 100
print(f'Meter ={meter} and Centemeter ={centemeter}.')