# bank_account_credit_and_debit--

class account:
    def __init__(self, initial):
        self.balance = initial

    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount


user_acc = account(0)
N = int(input())
while (N > 0):
    amount = int(input())
    if (amount > 0):
        user_acc.credit(amount)
    else:
        user_acc.debit(-amount)
    N -= 1
print(user_acc.balance)
