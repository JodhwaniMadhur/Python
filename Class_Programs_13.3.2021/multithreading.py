import os
import threading
from time import sleep
def Thread1(no1):
    print("Thread 1 is created")
    print("PID of Thread 1 is:",os.getpid())
    for i in range (1,no1):
        sleep(1)
        print("Thread 1:",i)

def Thread2(no1):
    print("Thread 2 is created")
    print("PID of Thread 2 is:",os.getpid())
    for i in range (1,no1):
        sleep(1)
        print("Thread 2:",i)

def main():
    print("Inside main")
    print("PID of current process is ",os.getpid())
    print("PID of parent process of main is ",os.getppid())
    value1=int(input())
    p1=threading.Thread(target=Thread1,args=(value1,))
    p2=threading.Thread(target=Thread2,args=(value1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("End of main process")

if __name__=="__main__":
    main()