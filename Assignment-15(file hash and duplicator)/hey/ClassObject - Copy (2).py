print("---- Marvellous Infosystems by Piyush Khairnar-----")

print("Demonstration of Class")

class Demo:

    def __init__(self,value1,value2):
        '''
        Just declaration and assigning of values to variables and methods in class
        '''
        print("Inside init method")
        self.i = value1
        self.j = value2
    
    def fun(self):
        print("Inside fun")
        print(self.i,self.j)

    def add(self):
        print(self.i + self.j)

# Create object of Demo class
obj1 = Demo(10,20)

# Call the method fun
obj1.fun()

# Create object of Demo class
obj2 = Demo(50,60)

# Call the method fun
obj2.fun()

# Call method Add to perform addition of characteristics
obj1.add()
obj2.add()
