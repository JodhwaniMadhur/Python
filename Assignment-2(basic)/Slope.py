def SlopePattern(num):
    i=num
    while i>0:
        j=0
        while j<i:
            print("*",end=" ")
            j=j+1
        print()
        i=i-1

no=int(input())
SlopePattern(no)