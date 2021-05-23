print("---- Marvellous Infosystems by Piyush Khairnar-----")

print("Demonstration of Advanced Functions")

# Function which accepts nothing and return nothing

def Marvellous1():
    print("Inside Marvellous1")

# Function which accepts value and return nothing

def Marvellous2(value):
    print("Inside Marvellous2")
    print("Accepted value is ",value)

# Function which accepts value and return value

def Marvellous3(value):
    print("Inside Marvellous3")
    print("Accepted value is ",value)
    return value+1

# Function which accepts multiple values and return multiple values

def Marvellous4(value1, value2):
    print("Inside Marvellous4")
    add = value1 + value2
    sub = value1 - value2
    return add,sub

# Function which calls another funnction which is defined outside it.

def Marvellous5():
    print("Inside Marvellous5")
    Marvellous1()

# Function which contains another nested funnction defined in it.

def Marvellous6():
    print("Inside Marvellous6")
    def InnerFun():
        print("Inside InnerFun")
    InnerFun()

# Function calls for above functions
no = 11

Marvellous1()
Marvellous2(no)
ret = Marvellous3(no)
print("Return value is ", ret)

Marvellous5()

ret1,ret2 = Marvellous4(10,4)
print("Addition is",ret1)
print("Substraction is", ret2)
