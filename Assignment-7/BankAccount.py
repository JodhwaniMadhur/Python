class BankAccount:
    ROI=10.5
    def __init__(self,name,amount):
        self.Name=name
        self.Amount=amount

    def Display(self):
        print(self.Name)
        print(self.Amount)
        print(self.ROI)

    def Deposit(self):
        print("enter amount:")
        da=int(input())
        self.Amount+=da

    def Withdraw(self):
        print("enter amount:")
        self.Amount=self.Amount-int(input())

    def CalculateIntrest(self):
        self.ROI=BankAccount.ROI*self.Amount

def main():
    obj1=BankAccount("Madhur",5000)
    obj2=BankAccount("Komal",7654)
    obj1.CalculateIntrest()
    obj2.CalculateIntrest()
    obj1.Deposit()
    obj2.Withdraw()
    obj1.Display()
    obj2.Display()

if __name__=="__main__":
    main()