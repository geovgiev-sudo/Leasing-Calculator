# Входни данни
principal = float(input("Въведи сума на кредита (лв): "))
annual_interest_rate = float(input("Годишна лихва (%): "))
years = int(input("Срок на кредита (в години): "))

# Преобразуване на годишната лихва в месечна
monthly_interest_rate = annual_interest_rate / 100 / 12
months = years * 12

# Формула за месечна вноска (анюитет)
monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1)

# По-четлива таблица
print("\n" + "=" * 72)
print(f"{'Месец':<8} | {'Вноска':<12} | {'Лихва':<12} | {'Главница':<12} | {'Остатък':<12}")
print("-" * 72)

remaining_balance = principal

for month in range(1, months + 1):
    interest = remaining_balance * monthly_interest_rate
    principal_paid = monthly_payment - interest
    remaining_balance -= principal_paid

    if remaining_balance < 0:
        remaining_balance = 0

    print(f"{month:<8} | "
          f"{monthly_payment:<12.2f} | "
          f"{interest:<12.2f} | "
          f"{principal_paid:<12.2f} | "
          f"{remaining_balance:<12.2f}")

print("=" * 72)
