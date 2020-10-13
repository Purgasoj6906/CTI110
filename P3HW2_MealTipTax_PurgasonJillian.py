# CTI-110
# P3HW2 - MealTipTax
# Purgason, Jillian
# 09/28/2020
#

meal_cost = float(input('Please enter cost of meal:')) #user to enter cost of meal
tip_entered = int(input('Enter tip amount of 15, 18, or 20:'))# Tip Percentage

tax = float(6.0) # Sales Tax
tax_total = (tax / 100) * meal_cost

if tip_entered == 15:
    tip_total = (tip_entered / 100) * meal_cost #total tip
    meal_total = meal_cost + tip_total + tax_total # total cost of meal with tip and tax
    print()
    print('Meal price:', "{:.2f}".format(meal_cost)) # Meal price formatted to 2 decimal spots
    print('Tax:', "{:.2f}".format(tax_total))       # Total Tax formatted to 2 decimal spots
    print('Tip:', "{:.2f}".format(tip_total))       # Total Tip formatted to 2 decimal spots
    print('Total:', "{:.2f}".format(meal_total))     # Total Meal Cost with tax and tip formatted to 2 decimal spots
    
elif tip_entered == 18:
    tip_total = (tip_entered / 100) * meal_cost #total tip
    meal_total = meal_cost + tip_total + tax_total # total cost of meal with tip and tax
    print()
    print('Meal price:', "{:.2f}".format(meal_cost))
    print('Tax:', "{:.2f}".format(tax_total))
    print('Tip:', "{:.2f}".format(tip_total))
    print('Total:', "{:.2f}".format(meal_total))

elif tip_entered == 20:
    tip_total = (tip_entered / 100) * meal_cost #total tip
    meal_total = meal_cost + tip_total + tax_total  # total cost of meal with tip and tax
    print()
    print('Meal price:', "{:.2f}".format(meal_cost))
    print('Tax:', "{:.2f}".format(tax_total))
    print('Tip:', "{:.2f}".format(tip_total))
    print('Total:', "{:.2f}".format(meal_total))

else:
    print('error') #error prints whenever a different tip amount is enterred besides 15,18,20
    
