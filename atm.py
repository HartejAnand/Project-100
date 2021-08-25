class Atm():
    def __init__(self, account, owner, money):
        self.money=money
        self.account=account
        self.owner=owner
    def seeInfo(self):
        print("account number",self.account,"owned by:",self.owner)
        print("Total balance:",self.money)
    def deposit(self):
        d=input("how much do you want to add? ")
        print("New balance:",self.money,"+",d)
    def withdraw(self):
        s=input("how much do you want to take out? ")
        print("New balance:",self.money,"-",s)

atm1=Atm(5,"Hartej", 10000)

atm1.seeInfo()
atm1.deposit()
atm1.withdraw()