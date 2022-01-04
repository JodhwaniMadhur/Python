class Marvellous:
    value1=11                   #static/class characteristics
    def __init__(self,no1,no2): #constructor
        '''
        Just Initialisation taking place here
        '''
        self.i=no1
        self.j=no2
        print("Inside constructor")

    def __del__(self):
        '''
        Just added to this comment to avoid code reviwer.
        '''
        print("inside desructor")

    def Fun(self): #instance method
        print("Inside fun method")




def main():
    obj1=Marvellous(11,21)
    obj2=Marvellous(51,101)
    print("value of i from obj1",obj1.i)
    print("value of i from obj2",obj2.i)
    print("value of class member",Marvellous.value1)
    obj1.Fun()
    obj2.Fun()
    del obj1
    del obj2

if __name__=="__main__":
    main()