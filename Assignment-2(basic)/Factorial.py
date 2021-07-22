def Factorial(num):
    i=1
    while num>0:
        i=i*num
        num=num-1
    return i

no=int(input())
ans=Factorial(no)
print(ans)