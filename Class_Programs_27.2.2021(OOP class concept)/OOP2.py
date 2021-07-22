def Add(no1,no2):
    return no1+no2

def Sub(no1,no2):
    return no1-no2


def main():
    print("Enter first number")
    val1=int(input())
    print("Enter Second Number")
    val2=int(input())
    ret=Add(val1,val2)
    print(ret)
    ret2=Sub(val1,val2)
    print(ret2)
    
if __name__=="__main__":
    main()