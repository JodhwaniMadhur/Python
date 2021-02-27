import heapq
ans=lambda data:heapq.nlargest(1,data)

def MaxElement(data):
    temp=0
    i=0
    while i < len(data):
        if temp < data[i]:
            temp=data[i]
        i=i+1
    return temp

arr=[]
print("Enter number of elements in the list")
no=int(input())
i=0
while i < no:
    print("Enter value for element no:",i+1)
    arr.append(int(input()))
    i+=1
print("Largest element in the list is:",MaxElement(arr))
print("Largest element in the list is:",ans(arr))
