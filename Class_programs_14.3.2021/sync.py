import threading

amount=1000

def ATM(func,lock):
    func(lock)


def Withdraw(lock):
    value=int(input("Enter the amount to withdraw"))
    global amount
    lock.acquire()
    if value>amount:
        print("There is no sufficient balance")
    else: 
        amount-=value
        print("Withdraw successful - Balance: ",amount)
    lock.release()


def Deposit(lock):
    value=int(input("Enter the amount to deposit"))
    global amount
    lock.acquire()
    amount=amount+value
    print("Deposit successful-Balance: ",amount)
    lock.release()
    



def main():
    print("Inside main")
    lock=threading.Lock()
    t1=threading.Thread(target=ATM,args=(Deposit,lock,))
    t2=threading.Thread(target=ATM,args=(Withdraw,lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("ATM application closed")

if __name__=="__main__":
    main()