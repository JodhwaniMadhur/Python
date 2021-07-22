

def Filter(values):
    i=0
    while i < len(values):
        if values[i]>=70 and values[i]<=90:
            brr.append(values[i])
        i=i+1


def Map(data):
    i=0
    while i < len(data):
        data[i]=data[i]+10
        i=i+1



def Reduce(data):
    product=1
    i=0
    while i<len(data):
        product=product*data[i]
        i=i+1
    return product

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
Filter(arr)
print("Data after Filter is:",brr)
Map(brr)
print("Data after Map is:",brr)
print("Data after Reduce is",Reduce(brr))
