def PrintNums(num):
    i=0
    while i<num:
        j=1
        while j<=num:
            print(j,end=" ")
            j=j+1
        print()
        i=i+1

no=int(input())
PrintNums(no)