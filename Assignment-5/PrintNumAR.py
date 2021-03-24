i=1
def NumsAscending(value):
    global i
    if i<=value:
        print(i,end=" ")
        i=i+1
        NumsAscending(value)

no=int(input())
NumsAscending(no)