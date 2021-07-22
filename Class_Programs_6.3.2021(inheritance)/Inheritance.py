class Base:
    def __init__(self):
        self.i=10
        self.j=20
        
    def fun(self):
        print("inside Base fun")

    def gun(self):
        print("Inside base gun")
    
class Derived(Base):
    def __init__(self):
        Base.__init__(self)#####Important### is like super in java
        self.x=30#for calling base instance varibales we need to call base constructor from derived
        self.y=40
        print("Inside derived constructor")
    
    def sun(self):
        print("inside derived sun")

    def gun(self):#overriding here
        print("Inside Derived gun")

    
def main():
    bobj=Base()
    print(bobj.i)
    print(bobj.j)
    bobj.fun()
    bobj.gun()
    dobj=Derived()

    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    dobj.sun()
    dobj.gun()
    dobj.fun()
    

if __name__=="__main__":
    main()