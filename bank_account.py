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
        return self.__balance


account = BankAccount()
account.deposit(8000)
account.withdrawal(1800)
print(f"Текущий баланс: {account.get_balance()} руб.\n")
