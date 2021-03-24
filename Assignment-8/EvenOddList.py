import threading

def EvenFactors(value):
    sum_even=0
    print("Inside Even function")
    for i in range(0,len(value)):
        if value[i]%2==0:
            sum_even+=value[i]
    print(sum_even)
        
def OddFactors(value):
    sum_odd=0
    print("Inside Odd function")
    for i in range(0,len(value)):
        if value[i]%2!=0:
            sum_odd+=value[i]
    print(sum_odd)

def main():
    print("Inside Main")
    print("Enter Number of elements")
    no=int(input())
    arr=[]
    for i in range (0,no):
        arr.append(int(input()))
    t1=threading.Thread(target=EvenFactors,args=(arr,))
    t2=threading.Thread(target=OddFactors,args=(arr,))
    t1.start()
    t2.start()
    


if __name__=="__main__":
    main()