print("---- Marvellous Infosystems by Piyush Khairnar-----")

print("Demonstration of Function calling technique")

# Passing immutable values
def Fun(value):
    print("Input value : ",value)
    print("Id of input value", id(value))
    value = 11
    print("Changed Input value : ",value)
    print("Id of changed input value", id(value))

print("Demonstration of Immutable arguments")

no = 10
print("Parameter : ",no)
print("Id of parameter", id(no))

Fun(no)

print("Parameter  after frunction call: ",no)
print("Id of parameter after function call", id(no))

def Gun(valueList):
    print("Input list : ",valueList)
    print("Id of input list", id(valueList))
    valueList[0] = 11
    valueList[1] = 21
    print("Changed Input List : ",valueList)
    print("Id of changed input List", id(valueList))

print("Demonstration of Mutable arguments")

l = [10,20,30,40]
print("Contents of list before call",l)
print("Id of list before call ", id(l))

Gun(l)
print("Contents of list after call",l)
print("Id of list after call ", id(l))


