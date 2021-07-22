
def Print(value): 
    i=0
    if i != value:
        print("*",end=" ")
        value=value-1
        Print(value)

no=int(input())
Print(no)