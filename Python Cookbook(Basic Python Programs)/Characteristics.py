print("---- Marvellous Infosystems by Piyush Khairnar-----")

print("Demonstration of Characteristics of Class")

class Demo:
    x = 10
    
    def __init__(self,no1,no2):
        """Just initialization of variables taking place here"""
        self.i = no1
        self.j = no2

obj1 = Demo(10,20)
obj2 = Demo(11,21)

print(obj1.i)
print(obj1.j)

print(obj2.i)
print(obj2.j)

print(Demo.x)
