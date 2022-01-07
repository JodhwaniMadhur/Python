class Demo:
#python doesn't support method overloading
    def Add(self,no1,no2):
        return no1+no2
    
    def Add(self,no1,no2,no3):
        return no1+no2+no3



obj=Demo()
ret=obj.Add(10,22)
ret=obj.Add(10,20,30)
print(ret)