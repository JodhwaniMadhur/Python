a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

print(a.keys() & b.keys())
#intersection of 2 lists with only keys in common
print(a.keys()-b.keys())
#keys in a that are not in b
#a union b = a + b - a intersection b - b
print(a.items()&b.items())
#intersection of 2 lists with both keys and values in common