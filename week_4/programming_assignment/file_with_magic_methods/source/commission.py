class Value:
    def __init__(self):
        self.amount = 0

    def __set__(self, obj, value):
        self.amount = value * (1 - obj.commission)

    def __get__(self, instance, owner):
        return self.amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
#
#
# new_account = Account(0.1)
# new_account.amount = 100
#
# print(new_account.amount)
