class Base:
    def __init__(self):
        self.i=10
        self.j=20
        print("inside Base constructor")


class Derived1(Base):
    def __init__(self):
        Base.__init__(self)#####Important### is like super in java
        self.x=30#for calling base instance varibales we need to call base constructor from derived
        self.y=40
        print("Inside derived1 constructor")

class Derived2(Derived1):
    def __init__(self):
        Derived1.__init__(self)
        self.a=50
        self.b=60
        print("Inside derived2 constructor")




def main():
    dobj=Derived2()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    print(dobj.a)
    print(dobj.b)


if __name__=="__main__":
    main()