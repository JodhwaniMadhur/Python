import threading

def printOrder(value,lock):
    lock.acquire()
    print("Inside PrintOrderly Thread")
    for i in range(1,value+1):
        print("Thread PrintOrderly: ",i)
    lock.release()

def printReverse(value,lock):
    lock.acquire()
    print("Inside Print Reverse Thread")
    while(value!=0):
        print("Thread Printreverse: ",value)
        value-=1
    lock.release()

def main():
    print("Enter Number")
    no=int(input())
    lock=threading.Lock()
    t1=threading.Thread(target=printOrder,args=(no,lock,))
    t2=threading.Thread(target=printReverse,args=(no,lock,))
    t1.start()
    t2.start()
    print("End of Main")

if __name__=="__main__":
    main()