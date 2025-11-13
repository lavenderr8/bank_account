class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"На счёт внесено {amount} руб.\n")
        else:
            print("Сумма должна быть не менее 1 руб.\n")

    def withdrawal(self, amount):
        if amount <= 0:
            print(f"Сумма снятия должна быть положительной.\n")
        elif amount > self.__balance:
            print("На вашем счёте недостаточно средств.\n")
        else:
            self.__balance -= amount
            print(f"Со счёта списано {amount} руб.\n")

    def get_balance(self):
        print(f"Текущий баланс: {self.__balance} руб.\n")

def check_balance(account):
    account.get_balance()


def add_money(account):
    try:
        amount = float(input("Введите сумму для пополнения: "))
        account.deposit(amount)
    except ValueError:
        print("Ошибка: введите числовое значение.\n")


def withdraw_money(account):
    try:
        amount = float(input("Введите сумму для снятия: "))
        account.withdrawal(amount)
    except ValueError:
        print("Ошибка: введите числовое значение.\n")


def bank_menu(account):
    menu_options = {
        "1": ("Проверить баланс.", check_balance),
        "2": ("Пополнить счёт.", add_money),
        "3": ("Снять деньги.", withdraw_money),
    }

    while True:
        print("🏦 Меню банка:")
        for key, (desc, _) in menu_options.items():
            print(f"{key}. {desc}")
        print("0. Выход.\n")

        choice = input("Выберите действие: ").strip()

        if choice == "0":
            print("\nВыход из программы.")
            break

        if choice in menu_options:
            _, action = menu_options[choice]
            action(account)
        else:
            print("Некорректный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    user_account = BankAccount()
    bank_menu(user_account)