#name=lambda parameters:body
#normal function
def Addition(no1,no2):
    return no1+no2

#lambda function
ans=lambda no1,no2:no1+no2

def main():
    print("Enter first number")
    value1=int(input())
    print("Enter second number")
    value2=int(input())

    ret=Addition(value1,value2)
    print("Addition is",ret)
    l=ans(value1,value2)
    print("Addition with lambda is",l)

if __name__=="__main__":
    main()