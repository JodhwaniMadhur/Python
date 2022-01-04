#A priority queue is a common implementation of heap and is used for getting elements with highest priority first 
#and lowest priority last

import heapq

class PriorityQueue:
    def __init__(self):
        '''Just initialization here'''
        self._queue=[]
        self._index=0
  
def push(self,item,priority):
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1

def pop(self):
    return heapq.heappop(self._queue)[-1]