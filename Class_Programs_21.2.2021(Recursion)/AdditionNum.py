
global sumofvar
global i
i=0
sumofvar=0

def AddR(data):
    if i < len(data):
        sumofvar=sumofvar+data[i]
        i=i+1
        AddR(data)
    return sumofvar

arr=[]
print("Enter number of elements")
no=int(input())
for i in range(no):
    arr.append(int(input()))

ans=AddR(arr)
print(ans)