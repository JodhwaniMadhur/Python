fac=1
def Fact(value):
    global fac
    if value==0:
        print(fac)
    if value!=0:
        fac=fac*value
        value=value-1
        Fact(value)


no=int(input())
Fact(no)
