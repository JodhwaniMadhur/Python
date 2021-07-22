def Freq(value,data):
    i=0
    fre=0
    while i < len(data):
        if data[i]==value:
            fre=fre+1
        i=i+1
    return fre

arr=[]
print("Enter number of elements in the list")
no=int(input())
i=0
while i < no:
    print("Enter value for element no:",i+1)
    arr.append(int(input()))
    i+=1
print("Enter the number whose frequency is wanted")
value=int(input())
print("Frequency of",value,"in the list is:",Freq(value,arr))

