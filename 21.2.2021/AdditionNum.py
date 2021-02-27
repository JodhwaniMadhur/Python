
global sum
global i
i=0
sum=0

def AddR(data):
    if i < len(data):
        sum=sum+data[i]
        i=i+1
        AddR(data)
    return sum

arr=[]
print("Enter number of elements")
no=int(input())
for i in range(no):
    arr.append(int(input()))

ans=AddR(arr)
print(ans)