from array import array 
print("---- Marvellous Infosystems by Piyush Khairnar-----")

print("Demonstration of Array")

# Array is connsidered as collection of Homogeneous elements
# As there is no direct support for array in python we have to import array module to create array

import array as arr
from array import array

a = arr.array('i', [2, 4, 6, 8])    # is is considered as type code

print("First element:", a[0])
print("Second element:", a[1])
print("Second last element:", a[-1])


a = arr.array('f', [2.4, 4.5, 6.5, 8.8])    # is is considered as type code


print("First element:", a[0])
print("Second element:", a[1])
print("Second last element:", a[-1])


print(a.typecode)

a.reverse()
for i in range(len(a)):
    print(a[i])

b = array('i',[1,2,1,2])
for i in range(len(b)):
    print(b[i])


i =0
while (i<len(b)):
    print(b[i])
    i+=1

