import threading

def Even(value):
    print("Inside Even function")
    for i in range(1,2*value):
        if i%2==0:
            print(i)
        
def Odd(value):
    print("Inside Odd function")
    for i in range(1,2*value):
        if i%2!=0:
            print(i)

def main():
    print("Inside Main")
    print("Enter Number")
    no=int(input())
    t1=threading.Thread(target=Even,args=(no,))
    t2=threading.Thread(target=Odd,args=(no,))
    t1.start()
    t2.start()


if __name__=="__main__":
    main()