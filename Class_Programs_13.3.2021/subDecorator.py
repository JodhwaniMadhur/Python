def main():
    #print("Enter first number")
    #value1=int(input())
    #print("Enter second number")
    #value2=int(input())
    ret=subDecorator(subraction)
    print("Subraction is:",ret)
    

#inbuilt function from module
def subraction(no1,no2):
    return no1-no2

def subDecorator(func_name): #function pointer type
    return func_name(10,5)

if __name__=="__main__":
    main()