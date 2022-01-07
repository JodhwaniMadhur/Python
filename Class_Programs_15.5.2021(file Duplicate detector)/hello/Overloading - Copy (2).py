from typing import overload


class Demo:
#python doesn't support method overloading
    def Add(self,no1,no2):
        return no1+no2
    
    @overload
    def Add(self,no1,no2,no3):
        return no1+no2+no3


    
obj=Demo()
ret=obj.Add(10,22)
print(ret)