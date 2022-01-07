class Arithmetic:
    def __init__(self,no):
        self.Value=no
        
    def ChkPrime(self):
        if self.Value > 1:
            for i in range(2, self.Value):
                if (self.Value % i) == 0:
                    print(self.Value, "is not a prime number")
                    break
        else:
            print(self.Value, "is not a prime numberber")

    def ChkPerfect(self):
        sumofvar = 0
        for x in range(1, self.Value):
            if self.Value % x == 0:
                sumofvar += x

        if(sumofvar==self.Value):
            print(self.Value,end=" ")
            print("is a Perfect Number")
        else:
            print(self.Value,end=" ")
            print("is not a Perfect Number")

    def printFactors(self):
        i=1
        while(i<self.Value):
            if(self.Value%i==0):
                print(i,end=" ")
            i=i+1
        print()

    def FactorSum(self):
        sumofvar = 0
        for x in range(1, self.Value):
           if self.Value % x == 0:
               sumofvar += x
        print("Sum of Factors is:",sumofvar)

def main():
    obj1=Arithmetic(65)
    obj2=Arithmetic(54)
    obj1.ChkPrime()
    obj1.ChkPerfect()
    obj1.printFactors()
    obj1.FactorSum()
    obj2.ChkPrime()
    obj2.ChkPerfect()
    obj2.printFactors()
    obj2.FactorSum()


if __name__=="__main__":
    main()