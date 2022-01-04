

def chkprime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    else:
        return True

def max(values):
    i=0
    maxvar=0
    while i<len(values):
        if maxvar<values[i]:
            maxvar=values[i]
        i=i+1
    return maxvar

arr=[]
brr=[]
print("Enter number of elements in the list")
no=int(input())
i=0
while i < no:
    print("Enter value for element no:",i+1)
    arr.append(int(input()))
    i+=1
print("Entered data is:",arr)
i=0
while i < len(arr):
    if chkprime(arr[i])==True:
        brr.append(arr[i])
    i=i+1
print("Data after Filter is:",brr)
newdata2=list(map(lambda no:(no*2),brr))
print("Data after Map is:",newdata2)
print("Data after Reduce is",max(newdata2))