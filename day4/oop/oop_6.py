
class bank:

    def __init__(self, i, ob, n):
        print("inside init")
        self.cid = i
        self.open_bal = ob
        self.cust_name = n
        self.cur_bal = ob

    def display(self):
        print("welcome", self.cust_name)
        print("your current balance is =", self.cur_bal)

    def deposit(self, amt):
        self.cur_bal = self.cur_bal + amt
        print("we have deposited", amt, "in your account")

    def withdraw(self, amt):
        if self.cur_bal < amt:
            print("insufficient balance")
        else:
            self.cur_bal = self.cur_bal - amt
            print("thank you for banking with us")

obja = bank(34560, 1000, "joe biden")
objb = bank(34562, 1200, "yoshihide suga")

