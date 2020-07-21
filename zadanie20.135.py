class Result:
    def __init__(self, ifSuccess, message, actualBalance=None):
        self.ifSucess = ifSuccess
        self.message = message
        self.actualBalance = actualBalance

class BankAccount:
    user_id = 1
    def __init__(self, balance = 0):
        self.balance = balance
        self.user_id = BankAccount.user_id
        BankAccount.user_id += 1
    def deposit(self, value):
        self.balance += value
        return self.balance
    def try_withdraw(self, value):
        if (self.balance > value):
            self.balance -= value
            return Result(True, "Wyplata powiodla sie", self.balance)
        return Result(False, "Wyplata nie powiodla sie", self.balance)
    def check_balance(self):
        print(self.balance)



konto = BankAccount(1000)

konto.deposit(500)

result = konto.try_withdraw(2000)
if result.ifSucess == True:
    print("{}. Aktualny stan konta wynosi {}".format(result.message ,
                                                     result.actualBalance))
else:
    print("{}. Aktualny stan konta wynosi {}".format(result.message ,
                                                     result.actualBalance))
konto.check_balance()


