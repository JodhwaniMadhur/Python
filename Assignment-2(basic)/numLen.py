def numLen(num):
    i=0
    while num != 0:
        i=i+1
        num=num//10
    print(i)

no=int(input())
numLen(no)