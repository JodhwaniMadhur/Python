# Design object oriented python application which accepts N numbers from user and
# perform below operations
# Display all even nunmbers
# calculate the summation of all numbers
# Display all perfect numbers

class Numbers:
    def __init__(self,no = 10):
        """
        initialization taking place here
        """
        self.size = no
        self.arr = []

    def __del__(self):
        """
        Nothin much happening here, just deallocation of resources
        taking place here.
        """
        print("Dealocating the memory of object")
        del self.arr

    def Accept(self):
        print("Please enter the elements")
        for i in range(self.size):
            print("Enter number : ",i + 1)
            self.arr.append(int(input()))

    def Display(self):
        print("Elements of list are")
        for i in range(self.size):
            print(self.arr[i])
 
    def Summation(self):
        sum_of_var = 0
        for i in range(self.size):
            sum_of_var = sum_of_var + self.arr[i]
        return sum_of_var

    def EvenDisplay(self):
        print("Even elemnets from list are :")
        for i in range(self.size):
            if (self.arr[i] % 2) == 0:
                print(self.arr[i])

    def PerfectDisplay(self):
        sum_of_var = 0
        for i in range(self.size):
            for j in range(1,int(self.arr[i]/2)+1):
                if (self.arr[i] % j) == 0:
                    sum_of_var = sum_of_var + j
            if sum_of_var == self.arr[i]:
                print(self.arr[i])
            sum_of_var = 0

    def PrimeDisplay(self):
        Flag = False
        for i in range(self.size):
            for j  in range(2,int(self.arr[i]/2)+1):
                if(self.arr[i] %j) == 0:
                    Flag = True
                    break
            if Flag == False:
                print(self.arr[i])
            Flag = False
    
def main():
    print("Enter number of elements")
    value = int(input())
    
    obj1 = Numbers(value)
    obj1.Accept()
    obj1.Display()
    ret = obj1.Summation()
    print("Summation of all elements :",ret)
    obj1.EvenDisplay()
    print("Perfect numbers are : ")
    obj1.PerfectDisplay()
    print("Prime nummbers are")
    obj1.PrimeDisplay()
    del obj1

if __name__ == "__main__":
    main()