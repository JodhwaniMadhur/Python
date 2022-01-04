class Circle:
    pi=3.14
    def __init__(self):
        '''
        Declaration of variables taking place here. 
        '''
        self.Area=0.0
        self.Circumference=0.0
        
    def Accept(self):
        print("Enter value of radius")
        self.radius=float(input())

    def CalculateArea(self):
        self.Area=self.pi*self.radius*self.radius

    def CalculateCircumference(self):
        self.Circumference=self.pi*self.radius
    
    def Display(self):
        print(self.radius)
        print(self.Area)
        print(self.Circumference)

def main():
    obj1=Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

if __name__ =="__main__":
    main()
    