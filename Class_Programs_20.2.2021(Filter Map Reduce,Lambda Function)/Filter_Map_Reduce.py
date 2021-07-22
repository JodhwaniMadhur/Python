#Accept N numbers from user and filterout even numbers from it and 
# filterout even numbers and increment 2 to each even number
#and return the summation of all the numbers.
#input:[1,2,3,4,5,6,7,8,9]
#filter:[2,4,6,8]
#map:[4,6,8,10]
#output:28

def CheckEven(no):
    if no%2==0:
        return True
    else :
        return False

#filter function
def MarvellousFilter(arr):
    brr=[]
    for i in range(len(arr)):
        if CheckEven(arr[i])==True:
            brr.append(arr[i])
    
    return brr
#this is map function
def MarvellousMap(brr):
    for i in range(len(brr)):
        brr[i]=brr[i]+2
    return brr


#this is reduce function
def Sum(brr):
    sum=0
    for i in range(len(brr)):
        sum=sum+brr[i]
    return sum


def main():
    arr=[]
    print("Enter number of elements")
    size=int(input()) 
    for i in range(size):
        print("Enter element number:",i+1)
        no=int(input())
        arr.append(no)

    print("Your entered data is:",arr)
    newdata=MarvellousFilter(arr)
    print(newdata)
    new=MarvellousMap(newdata)
    print(new)
    ans=Sum(new)
    print("Summation is:",ans)


if __name__ == "__main__":
    main()
