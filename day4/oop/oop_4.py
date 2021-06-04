# OOP

class bank:
    cid = 23
    current_balance = 2000
    
    def funca(self):
        print("hello from funca in bank")

    def display(self):
        print("cid =", self.cid)
        print("current balance =", self.current_balance)

    def funcx():
        print("hey")
 

obja = bank()
objb = bank()

#error
obja.funcx()
    # bank.funcx(obja)
