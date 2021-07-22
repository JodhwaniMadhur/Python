import math

def SumF(num):
    if num==1:
        return 1
    sum=0
    for i in range(2,(int)(math.sqrt(num))+1):
        if num%i==0:
            if i==(num/i):
                sum=sum+i
            else:
                sum=sum+(i+num//i)
    return sum+1

no=int(input())
ans=SumF(no)
print(ans)
