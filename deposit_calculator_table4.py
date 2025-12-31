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

# Предсрочно погасяване
extra_payment_option = input("Искаш ли предсрочно погасяване? (да/не): ").lower()

extra_month = None
extra_amount = 0

if extra_payment_option == "да":
    extra_month = int(input("В кой месец ще направиш предсрочно погасяване?: "))
    extra_amount = float(input("Каква сума ще внесеш допълнително (лв)?: "))

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

    # Лихва и главница
    interest = remaining_balance * monthly_interest_rate
    principal_paid = monthly_payment - interest
    remaining_balance -= principal_paid

    # Проверка за предсрочно погасяване
    if extra_month is not None and month == extra_month:
        print(BOLD + MAGENTA + "\n>>> Извършено предсрочно погасяване!" + RESET)
        remaining_balance -= extra_amount
        if remaining_balance < 0:
            remaining_balance = 0

    if remaining_balance < 0:
        remaining_balance = 0

    # Печат
    print(
        f"{YELLOW}{month:<8}{RESET} | "
        f"{GREEN}{monthly_payment:<12.2f}{RESET} | "
        f"{MAGENTA}{interest:<12.2f}{RESET} | "
        f"{CYAN}{principal_paid:<12.2f}{RESET} | "
        f"{BLUE}{remaining_balance:<12.2f}{RESET}"
    )

    if remaining_balance == 0:
        break

print(BOLD + BLUE + "=" * 72 + RESET)
