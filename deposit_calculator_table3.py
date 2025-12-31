# Цветове (ANSI escape codes)
RESET = "\033[0m"
BOLD = "\033[1m"

CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"

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
print("\n" + BOLD + BLUE + "=" * 72 + RESET)
print(f"{BOLD}{CYAN}{'Месец':<8} | {'Вноска':<12} | {'Лихва':<12} | {'Главница':<12} | {'Остатък':<12}{RESET}")
print(BLUE + "-" * 72 + RESET)

remaining_balance = principal

for month in range(1, months + 1):
    interest = remaining_balance * monthly_interest_rate
    principal_paid = monthly_payment - interest
    remaining_balance -= principal_paid

    if remaining_balance < 0:
        remaining_balance = 0

    print(
        f"{YELLOW}{month:<8}{RESET} | "
        f"{GREEN}{monthly_payment:<12.2f}{RESET} | "
        f"{MAGENTA}{interest:<12.2f}{RESET} | "
        f"{CYAN}{principal_paid:<12.2f}{RESET} | "
        f"{BLUE}{remaining_balance:<12.2f}{RESET}"
    )

print(BOLD + BLUE + "=" * 72 + RESET)
