current_price = int(input())
last_months_price = int(input())

change_in_price = (current_price - last_months_price)
est_mortg = (current_price*0.051/12)

print('This house is ${0}. The change is ${1} since last month.'.format(current_price, change_in_price))
print('The estimated monthly mortgage is ${:.2f}.'.format(est_mortg))

   