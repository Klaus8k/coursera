class Value:
    def __init__(self):
        self.amount = 0


    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        self.amount = value * (1 - instance.commission)




class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
        # self.ballance = 0

# new_account = Account(0.5)
# new_account.amount = 200
# new_account.amount = 100
#
# new_account.amount = 300
# print(new_account.amount)