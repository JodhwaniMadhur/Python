class Demo:
    def __init__(self,i,j):
        self.no1=i
        self.no2=j
        
    def Fun(self):
        print(self.no1)
    
    def Gun(self):
        print(self.no2) 

def main():
    obj=Demo(11,21)
    obj2=Demo(51,101)
    obj.Fun()
    obj2.Fun()
    obj.Gun()
    obj2.Gun()

main()