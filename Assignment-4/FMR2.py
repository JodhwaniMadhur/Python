import functools

arr=[]
print("Enter number of elements in the list")
no=int(input())
i=0
while i < no:
    print("Enter value for element no:",i+1)
    arr.append(int(input()))
    i+=1
print("Entered data is:",arr)
newdata1=list(filter(lambda no1:(no1%2==0),arr))
print("Data after Filter is:",newdata1)
newdata2=list(map(lambda no:(no**2),newdata1))
print("Data after Map is:",newdata2)
ans=functools.reduce(lambda no1,no2: no1 + no2, newdata2)
print("Data after Reduce is",ans)