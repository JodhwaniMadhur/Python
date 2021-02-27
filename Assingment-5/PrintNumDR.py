i=0
def PrintNumsD(value):
    global i
    if value!=i:
        print(value,end=" ")
        value=value-1
        PrintNumsD(value)

no=int(input())
PrintNumsD(no)