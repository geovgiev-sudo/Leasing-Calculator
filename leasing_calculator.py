print(f'Please enter currency')
currency = input('>>>')
print(f'Please enter percentage interest rate')
percentage_interest_rate = float(input('>>>'))
print(f'Please enter total sum')
total_sum = float(input('>>>'))
print(f'Please enter months')
period_months = int(input('>>>'))
total_sum_interest = total_sum + ((percentage_interest_rate / 100) * total_sum)
monthly_payment = total_sum_interest / period_months
print(f'Your monthly payment will be {monthly_payment:.2f} {currency}.')

remaining_money_owed = 0
months_paid = 0
new_sum_interest = total_sum_interest

for i in range(period_months):
    months_left = period_months - months_paid
    print(f'You have the option to pay your leasing prematurely.')
    print(f'Would you like to take it?')
    option_premature = input('>>>')

    if option_premature == 'Yes':
        remaining_money_owed = new_sum_interest
        print(f'Great! You have chosen to finish prematurely! You owe us {remaining_money_owed} {currency}.')
        premature_fee = 69
        premature_total = (premature_fee / 100 * remaining_money_owed) + remaining_money_owed
        print(f'However, there is a fee for finishing prematurely.')
        print(f'You will need to pay an additional fee of {premature_fee}% per monthly payment.')
        print(f'Your total will be {premature_total:.2f}.')
        print(f'Are you sure you want to continue?')
        confirmation = input('>>>')
        if confirmation == 'Yes':
            print(f'Great! Please enjoy your premature payment. Have a great day!')
            break
        else:
            print(f'Looks like you are still not ready to finish. {months_left} months left to pay. Keep pumping!')
    else:
        remaining_money_owed = new_sum_interest
        print(f'Remaining money owed: {remaining_money_owed} {currency} for {months_left} months more.')

    new_sum_interest -= monthly_payment
    months_paid += 1