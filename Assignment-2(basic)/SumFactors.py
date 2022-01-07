import math

def SumF(num):
    if num==1:
        return 1
    sum_of_var=0
    for i in range(2,(int)(math.sqrt(num))+1):
        if num%i==0:
            if i==(num/i):
                sum_of_var=sum_of_var+i
            else:
                sum_of_var=sum_of_var+(i+num//i)
    return sum_of_var+1

no=int(input())
ans=SumF(no)
print(ans)
