import functools

def ChkPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
           return True
    else:
        return True

def Max(values):
    i=0
    max=0
    while i<len(values):
        if max<values[i]:
            max=values[i]
        i=i+1
    return max

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
    if ChkPrime(arr[i])==True:
        brr.append(arr[i])
    i=i+1
print("Data after Filter is:",brr)
newdata2=list(map(lambda no:(no*2),brr))
print("Data after Map is:",newdata2)
print("Data after Reduce is",Max(newdata2))