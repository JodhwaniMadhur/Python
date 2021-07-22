from collections import deque

q=deque(maxlen=3)
q.append(1)#we cannot specify more than argument to append even though they are seperated by ,
q.append(2)
q.append(3)
print(q) #output:deque([1, 2, 3], maxlen=3)
#if we fill more elements than max length of deque then it pops element from first and adds new element at last.
q.append(4)
q.append(5)
print(q)#output:deque([3, 4, 5], maxlen=3)
q.appendleft(6)
print(q)#output:deque([6, 4, 5,], maxlen=3)