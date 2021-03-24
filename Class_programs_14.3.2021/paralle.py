import os
import time
import multiprocessing

def Square(no):
    return no*no
################################################
def SerialProcessing():
    start=time.time()
    print("Inside serial processing")
    arr=range(100)
    ret=[]
    for i in arr:
        ret.append(Square(i))
    #print(ret)
    end=time.time()
    print("Serial Processing: ",end-start)
###############################################
def ParallelProcessing():
    start=time.time()
    print("Inside Parallel processing")
    arr=range(100)
    ret=[]
    pobj=multiprocessing.Pool()
    ret=pobj.map(Square,arr)
    end=time.time()
    print("Parallel execution:",end-start)


#########################################
def main():
    print("Inside main")
    ParallelProcessing()
    SerialProcessing()

if __name__=="__main__":
    main()