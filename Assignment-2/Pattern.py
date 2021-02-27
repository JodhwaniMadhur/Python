def Pattern(num):
    i=0
    while i<num:
        j=0
        while j<num:
            print("*",end=" ")
            j=j+1
        print()
        i=i+1

no=int(input())

Pattern(no)