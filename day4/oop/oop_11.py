
class bank:

    def __init__(self, i, ob=0, n="ashok kumar"):
        print("inside init")
        self.cid = i
        self.open_bal = ob
        self.cust_name = n
        self.cur_bal = ob

    def __grade(self):
        if self.cur_bal < 2000:
            self.__g = 'D'
        elif self.cur_bal >= 2000 and self.cur_bal < 10000:
            self.__g = 'C'
        else:
            self.__g = 'B'

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
            
    def loan_req(self):
        self.__grade()
        if self.__g == 'D':
            self.loan = self.cur_bal*1.5
        elif self.__g == 'B' or self.__g == 'C':
            self.loan = self.cur_bal*1.8
        elif self.__g == 'A':
            self.loan = self.cur_bal*2
        else:
            print("system error")
            return
        print("hello")
        print("you are eleigible for a loan of", self.loan)


obja = bank(34560, 1000, "joe biden")
objb = bank(34562, 1200, "yoshihide suga")
objc = bank(34564)

#     __  private
#       encapsulated
