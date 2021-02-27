import heapq

arr=[]
print("Enter number of elements in the list")
no=int(input())
i=0
while i < no:
    print("Enter value for element no:",i+1)
    arr.append(int(input()))
    i+=1
print("Entered data is:",arr)
heap=list(arr)
heapq.heapify(heap)
print(heapq.nlargest(3,arr))
#returns a new list which contains 1st,2nd,3rd largest element from the orignal list
print(heapq.nsmallest(3,arr))
#returns a new list which contains 1st,2nd,3rd smallest element from the orignal list
print(heap)
#the most important feature of heap is heap always has smallest element at first position and heapq.heappop()
#will always return smallest i.e first element from the left,heapify converts list into heap in linear time and space


portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
#prints smallest entries from the portfolio in the order of prices from small to large
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
#prints largest entries from the portfolio in order of price from large to small
print(expensive)