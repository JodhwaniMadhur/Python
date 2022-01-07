# Create Object of List
arr = list()

# Ask the user about the number of elements
num = input("Enter how many elements you want:")

print ("Enter numbers in array: ")

# Iterate the for loop to accept N numbers
for i in range(0,int(num)):
    # Accept individual element from user
    no = input("num :")
    # Insert that element into List
    arr.append(int(no))

print ("Entered elements are",arr)
