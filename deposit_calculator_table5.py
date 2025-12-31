# Цветове (ANSI escape codes)
RESET = "\033[0m"
BOLD = "\033[1m"

CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
RED = "\033[91m"

# Входни данни
principal = float(input("Въведи сума на кредита (лв): "))
annual_interest_rate = float(input("Годишна лихва (%): "))
years = int(input("Срок на кредита (в години): "))

# Опция за множество предсрочни погасявания (както беше)
extra_payments = {}

print("\nВъведи предсрочни погасявания.")
print("Пример: месец 12, сума 5000")
print("Когато приключиш, напиши 'стоп'.")

while True:
    command = input("Месец или 'стоп': ").lower()
    if command == "стоп":
        break
    month_number = int(command)
    amount = float(input("Сума за предсрочно погасяване (лв): "))
    extra_payments[month_number] = amount

# Преобразуване на годишната лихва в месечна
monthly_interest_rate = annual_interest_rate / 100 / 12
months = years * 12

# Формула за месечна вноска (анюитет)
monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1)

# Променливи за общи суми
total_interest_paid = 0
total_paid = 0

# Показване на месечната вноска
print("\n" + BOLD + GREEN + f"Месечна вноска: {monthly_payment:.2f} лв" + RESET)

# Заглавие на таблицата
print("\n" + BOLD + BLUE + "=" * 78 + RESET)
print(f"{BOLD}{CYAN}{'Месец':<8} | {'Вноска':<12} | {'Главница':<12} | {'Лихва':<12} | {'Остатък':<12} | {'Бележка':<12}{RESET}")
print(BLUE + "-" * 78 + RESET)

remaining_balance = principal

for month in range(1, months + 1):

    # Лихва и главница
    interest = remaining_balance * monthly_interest_rate
    principal_paid = monthly_payment - interest
    remaining_balance -= principal_paid

    # Натрупване на общи суми
    total_interest_paid += interest
    total_paid += monthly_payment

    note = ""

    # Проверка за предсрочно погасяване (както беше)
    if month in extra_payments:
        extra_amount = extra_payments[month]
        remaining_balance -= extra_amount
        note = f"{RED}Погасяване {extra_amount:.2f} лв{RESET}"
        if remaining_balance < 0:
            remaining_balance = 0

    if remaining_balance < 0:
        remaining_balance = 0

    # Печат на ред
    print(
        f"{YELLOW}{month:<8}{RESET} | "
        f"{GREEN}{monthly_payment:<12.2f}{RESET} | "
        f"{CYAN}{principal_paid:<12.2f}{RESET} | "
        f"{MAGENTA}{interest:<12.2f}{RESET} | "
        f"{BLUE}{remaining_balance:<12.2f}{RESET} | "
        f"{note:<12}"
    )

    if remaining_balance == 0:
        break

print(BOLD + BLUE + "=" * 78 + RESET)

# Показване на общите суми
print(BOLD + GREEN + f"\nОбщо платена сума: {total_paid:.2f} лв" + RESET)
print(BOLD + MAGENTA + f"Общо платена лихва: {total_interest_paid:.2f} лв" + RESET)
