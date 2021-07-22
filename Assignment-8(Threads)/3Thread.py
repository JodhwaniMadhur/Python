import os
import threading

def Small(value):
    print("PID of Small function thread is: ",os.getpid())
    count_small=0
    for i in range(0,len(value)):
        if ((value[i]>='a')and(value[i]<='z')):
            count_small+=1
    print(count_small)

def Capital(value):
    print("PID of Capital function thread is: ",os.getpid())
    count_capital=0
    for i in range(0,len(value)):
        if((value[i]>='A')and(value[i]<='Z')):
            count_capital+=1
    print(count_capital)


def Digits(value):
    print("PID of Digit function thread is: ",os.getpid())
    count_digits=0
    for i in range(0,len(value)):
        if((value[i]>='0') and (value[i]<='9')):
            count_digits+=1
    print(count_digits)
        
def main():
    print("Inside Main")
    print("PID of main function: ",os.getpid())
    print("PPID of main function: ",os.getppid())
    print("enter string")
    str=input()
    t1=threading.Thread(target=Small,args=(str,))
    t2=threading.Thread(target=Capital,args=(str,))
    t3=threading.Thread(target=Digits,args=(str,))
    t1.start()
    t2.start()
    t3.start()


if __name__=="__main__":
    main()