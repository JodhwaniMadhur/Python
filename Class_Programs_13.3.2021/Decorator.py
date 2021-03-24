def main():
    print("Enter first number")
    value1=int(input())
    print("Enter second number")
    value2=int(input())
    ret=subraction(value1,value2)
    print("Subraction is:",ret)

#inbuilt function from module
def subraction(no1,no2):
    return no1-no2

if __name__=="__main__":
    main()