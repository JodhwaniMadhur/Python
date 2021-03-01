print("---- Marvellous Infosystems by Piyush Khairnar-----")

print("Demonstration of List")

# List is considered as Array which contains Heterogenous data
#   Heterogeneous
#   Ordered
#   Indexed
#   Mutable
#   Allows Duplicate

batches = ["PPA","LB","Angular","Python"]

print(batches)
print(batches[0])
print(batches[1])
print(batches[-1])
print(batches[1:])
print(batches[:3])

# we can store heterogenious data
data1 = [11,"Marvellous",3.14]
print(data1)

data2 = [21,"Infosystems",6.10]

# We can create list of list

combined = [data1, data2]
print(combined)

# There are multiple methods that we can use to manipulate list

batches.append("MEAN")
print(batches)

batches.insert(2,"LSP")
print(batches)

batches.remove("LSP")
print(batches)

batches.pop()
print(batches)

batches.pop(2)
print(batches)

del batches[1:]
print(batches)


batches.extend(["LB","Python","Angular","MEAN"])
print(batches)

batches.sort()
print(batches)
