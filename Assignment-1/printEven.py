def PrintEven(num):
    i=1
    while i<=num*2:
        if i%2==0:
                print(i,end=" ")
        i=i+1

no=int(input())
PrintEven(no)