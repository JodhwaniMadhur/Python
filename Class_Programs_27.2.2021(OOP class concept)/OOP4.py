class Arithmetic:
    #self here is like this keyword in java
    #callback constructor like
    #calls itself
    def __init__(self,i,j):
        '''Just initialization of variables here'''
        print("Inside Constructor")
        self.no1=i
        self.no2=j
        
    def Add(self):
        return self.no1+self.no2
    
    def Sub(self):
        return self.no1-self.no2

def main():
    obj=Arithmetic(21,11) #__init__(obj1,21,11)
    obj2=Arithmetic(101,51)#__init__(obj2,101,51)
    print(obj.Add())
    print(obj2.Add())
    print(obj.Sub())
    print(obj2.Sub())

if __name__=="__main__":
    main()