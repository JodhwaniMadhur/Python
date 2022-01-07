import threading

def EvenFactors(value):
    sum_even=0
    print("Inside Even function")
    for i in range(1,(value//2)+1):
        if i%2==0:
            sum_even+=i
    print(sum_even)

def OddFactors(value):
    sum_odd=0
    print("Inside Odd function")
    for i in range(1,(value//2)+1):
        if i%2!=0:
            sum_odd+=i
    print(sum_odd)

def main():
    print("Inside Main")
    print("Enter Number")
    no=int(input())
    t1=threading.Thread(target=EvenFactors,args=(no,))
    t2=threading.Thread(target=OddFactors,args=(no,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("exit from main")


if __name__=="__main__":
    main()