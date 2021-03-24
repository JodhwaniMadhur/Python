#inbuilt function from module
def subraction(no1,no2):
    print("4:Inside Subraction")
    return no1-no2

def subDecorator(func_name): #function pointer type
    print("8:Inside subDecorator")
    def Updator(a,b):
        print("10:Inside Updator")
        if a<b: #if first parameter is small
            a,b=b,a
        return func_name(a,b)
    return Updator # returning object of Updator(this is being done by Decorator)

def main():
    print("17:Inside Main")
    sub=subDecorator(subraction) #return object of updator
    print("Enter first number")
    value1=int(input())
    print("Enter second number")
    value2=int(input())
    ret=sub(value1,value2)#updator object gets called internally
    print("Subraction is:",ret)
    print("24:End of Main")

if __name__=="__main__":
    print("27:Inside starter")
    main()
    print("29:End of Starter")


#sub -> updator ->subraction
#line:17 -> 6 -> 13->18 to 21 -> 22 -> 8 -> 9 to 11-> 12 ->2 to 4 -> 12 -> 22-> 23