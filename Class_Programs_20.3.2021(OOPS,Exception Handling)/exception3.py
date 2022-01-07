no1=int(input("Enter first number"))
no2=int(input("Enter second number"))
try:
    print("Inside try block")
    ans=no1/no2
except ZeroDivisionError as obj:
    print("Divide by zero exception",obj)
except Exception as eobj:
        print("Exception occurs",eobj)
else:
    print("Inside else block")
    print("Division is: ",ans)

finally:
    print("deallocate all resorces") 