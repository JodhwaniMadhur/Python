prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

min_value=min(zip(prices.values(),prices.keys()))
print(min_value)
#prints min value as per value
max_value=max(zip(prices.values(),prices.keys()))
print(max_value)
#prints max value as per values
prices_sorted=sorted(zip(prices.values(),prices.keys()))
#placing values first sorts them in ascending values and placing keys first sorts them according to lexicographical order
print(prices_sorted)
#When doing these calculations, be aware that zip() creates an iterator that can only be
#consumed once. For example, the following code is an error:

min_v=min(prices)
print(min_v)
#this will return minimum according to keys and not values
#output:AAPL
max_v=max(prices)
print(max_v)
#output=IBM