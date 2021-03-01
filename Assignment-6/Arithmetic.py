class Arithmetic:
    def Accept(self):
        print("Enter 1st number")
        self.no1=int(input())
        print("Enter second Number")
        self.no2=int(input())

    def Addition(self):
        return self.no1+self.no2

    def Subraction(self):
        return self.no1-self.no2
    
    def Multiplication(self):
        return self.no1*self.no2
    
    def Division(self):
        return self.no1/self.no2

def main():
    obj1=Arithmetic()
    obj1.Accept()
    print(obj1.Addition())
    print(obj1.Subraction())
    print(obj1.Multiplication())
    print(obj1.Division())

if __name__=="__main__":
    main()