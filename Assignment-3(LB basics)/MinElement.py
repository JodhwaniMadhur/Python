import heapq
ans=lambda data:heapq.nsmallest(1,data)

def MinElement(data):
    temp=0
    i=0
    while i < len(data):
        if temp>data[i]:
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
print("Smallest element in the list is:",MinElement(arr))
print("Smallest element in the list is:",ans(arr))