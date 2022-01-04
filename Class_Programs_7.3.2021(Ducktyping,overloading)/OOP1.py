#public no1
#protected _no2
#private __no3
class Base:
    def __init__(self):
        """Just initialization of variables taking place here."""
        self.no1=11
        self._no2=21
        self.__no3=51

    def fun(self):
        print(self.no1,self._no2,self.__no3)
    
    def _fun(self):
        print(self.no1,self._no2,self.__no3)
    
    def __fun(self):
        print(self.no1,self._no2,self.__no3)

class Derived(Base):
    def __init__(self):
        Base.__init__(self)

    def gun(self):
        print(self.no1)
        print(self._no2)
        #print(Base.__no3)
        self.fun()
        self._fun()
        #self.__fun()

def main():
    bobj=Base()
    print(bobj.no1,bobj._no2)
    bobj.fun()
    bobj._fun()
    #print(bobj.__fun())     #not allowed
    #bobj.__fun()            Not allowed
    dobj=Derived()
    dobj.gun()

    
if __name__=="__main__":
    main()