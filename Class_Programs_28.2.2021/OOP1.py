class Demo:
    x=10 #class variable
    y=20#common for all objects
    def __init__(self):
        print("Inside COnstructor")
        self.i=30 #instance variable
        #seperate for all objects
        self.j=40

    def __del__(self):
        print("Inside Destructor")

    def Fun(self):
        print("Inside fun")


def main():
    obj1=Demo()
    obj2=Demo()
    obj1.Fun()
    obj2.Fun()
    del obj1
    del obj2


if __name__=="__main__":
    main()