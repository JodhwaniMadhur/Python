def displayI(no):
    for i in range(no):
        print("Hello",i)


def Recursive(no):
    if no!=0:
        no=no-1
        print("hello",no)
        Recursive(no)

def main():
    print("Enter the number of iterations")
    value=int(input())
    print("Calling terative function")
    displayI(value)
    print("Calling Recursive function")
    Recursive(value)

if __name__=="__main__":
    main()