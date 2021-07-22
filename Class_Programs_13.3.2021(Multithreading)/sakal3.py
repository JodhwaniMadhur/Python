import os
import multiprocessing

def Process1(no1):
    for i in range (1,no1):
        print("Process 1:",i)

def Process2(no1):
    for i in range (1,no1):
        print("Process 2:",i)

def main():
    print("Inside main")
    print("PID of current process is ",os.getpid())
    print("PID of parent process of main is ",os.getppid())
    value1=int(input())
    p1=multiprocessing.Process(target=Process1,args=(value1,))
    p2=multiprocessing.Process(target=Process2,args=(value1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("End of main process")

if __name__=="__main__":
    main()