print(f'Please enter currency')
currency = input('>')
print(f'Please enter percentage interest rate')
percentage_interest_rate = float(input('>'))
print(f'Please enter total sum')
total_sum = float(input('>'))
print(f'Please enter months')
period_months = int(input('>'))

total_sum_interest = total_sum + ((percentage_interest_rate / 100) * total_sum)
monthly_payment = total_sum_interest / period_months

print(f'Your monthly payment will be {monthly_payment:.2f} {currency}.')