def SumList(data):
    ans=0
    for i in range (len(data)):
        ans=ans+data[i]
    return ans

arr=[]
print("Enter number of elements in the list")
no=int(input())
i=0
while i < no:
    print("Enter value for element no:",i+1)
    arr.append(int(input()))
    i+=1
print("Sum of all elements of the list is:",SumList(arr))