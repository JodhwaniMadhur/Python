class Demo:
#python doesn't support method overloading

    def Add(self,no1=None,no2=None,no3=None):
        if(no1!=None and no2!=None and no3!=None):
            return no1+no2+no3
        elif(no1!=None and no2!=None):
            return no1+no2
        elif(no1!=None):
            return no1
        else:
            return 0

    
obj=Demo()
ret=obj.Add(10,22,214)
print(ret)
ret=obj.Add(10,22)
print(ret)
ret=obj.Add(10)
print(ret)
ret=obj.Add()
print(ret)