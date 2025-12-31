# Входни данни
principal = float(input("Въведи сума на кредита (лв): "))
annual_interest_rate = float(input("Годишна лихва (%): "))
years = int(input("Срок на кредита (в години): "))

# Преобразуване на годишната лихва в месечна
monthly_interest_rate = annual_interest_rate / 100 / 12
months = years * 12

# Формула за месечна вноска (анюитет)
monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1)

# Заглавие
print("\nМесец | Вноска | Лихва | Главница | Остатък")
print("-----------------------------------------------")

remaining_balance = principal

# Генериране на таблицата
for month in range(1, months + 1):
    interest = remaining_balance * monthly_interest_rate
    principal_paid = monthly_payment - interest
    remaining_balance -= principal_paid

    if remaining_balance < 0:
        remaining_balance = 0

    print(f"{month:5d} | {monthly_payment:7.2f} | {interest:6.2f} | {principal_paid:8.2f} | {remaining_balance:8.2f}")
