
def ChkPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return True


arr=[]
brr=[]
sum=0
print("Enter number of elements in the list")
no=int(input())
i=0
while i < no:
    print("Enter value for element no:",i+1)
    arr.append(int(input()))
    i+=1
i=0
while i < no:
    if ChkPrime(arr[i])==True:
        brr.append(arr[i])
        sum=sum+arr[i]
    i=i+1
print(sum)
