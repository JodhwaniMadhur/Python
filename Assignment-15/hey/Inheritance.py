class A:
    def fun(self):
        print("Inside A fun")

class B(A):
    def gun(self):
        print("Inside B gun")

aobj = A()
bobj = B()

bobj.fun()
bobj.gun()

