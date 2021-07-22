import math

tc=int(input())
for i in range(tc):
    num=int(input())
    p,a=0,1
    while(num>=p):
        p=math.pow(2,a)
        a+=1
    a-=2
    A=math.pow(2,a)-1
    temp=p-num
    ans=A*(A+temp)
    print(ans)
