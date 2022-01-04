class Student:
    def __init__(self,str,a,b,c):
        """initialization taking place here"""
        self.name=str
        self.m1=a
        self.m2=b
        self.m3=c

    def __eq__(self,other):
        """Just returning of true or false here"""
        return self.m1==other.m1 and self.m2==other.m2 and self.m3==other.m3
            


def main():
    obj1=Student("Piyush",56,89,78)
    obj2=Student("Sarvesh",56,89,78)
    if obj1==obj2:
        print("Both the students are same")
    else:
        print("Both the students are different")

if __name__=="__main__":
    main()