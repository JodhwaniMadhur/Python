def PrintSlope(num):
    i=1
    while i<=num:
        j=1
        while j<=i:
            print(j,end=" ")
            j=j+1
        print()
        i=i+1

no=int(input())
PrintSlope(no)