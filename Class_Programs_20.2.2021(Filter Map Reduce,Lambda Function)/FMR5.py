# Accept N numbers from user and filterout only even numbers from that N numbers.
# After that add 2 in every even number.
# after the addition of 2 perform summation of that modified number.

# Input [1,3,2,4,6,5,4]

# After filter [2,4,6,4]
# after map [4,6,8,6]
# after reduce 24
    
import functools

def main():
    arr = []
    print("Enter number of elements")
    size = int(input())

    for i in range(size):
        print("Enter element number :",i+1)
        no = int(input())
        arr.append(no)

    print("Your entered data is :",arr)
    print(functools.reduce(lambda a,b:a+b,list(map(lambda no: no + 2, list(filter(lambda no: (no %2 == 0), arr))))))

if __name__ == "__main__":
    main()
