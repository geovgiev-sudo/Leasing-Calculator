# Входни данни
principal = float(input("Въведи сума на кредита (лв): "))
annual_interest_rate = float(input("Годишна лихва (%): "))
years = int(input("Срок на кредита (в години): "))

# Преобразуване на годишната лихва в месечна
monthly_interest_rate = annual_interest_rate / 100 / 12
months = years * 12

# Формула за месечна вноска (анюитетна формула)
monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1)

# Общо платена сума и лихва
total_paid = monthly_payment * months
total_interest = total_paid - principal

# Резултати
print("\n--- Резултати ---")
print(f"Месечна вноска: {monthly_payment:.2f} лв")
print(f"Общо платено: {total_paid:.2f} лв")
print(f"Общо лихва: {total_interest:.2f} лв")
