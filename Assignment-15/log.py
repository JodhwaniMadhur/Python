import hashlib
from sys import *
import os


def calculateCheckSum(path,blocksize=1024):
    fd=open(path,'rb')
    hobj=hashlib.md5()

    buffer=fd.read(blocksize)
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer=fd.read(blocksize)

    fd.close()
    return hobj.hexdigest()



def main():
    l=[]
    f=open("log.txt","wt")
    for Folder,Subfolder,File in os.walk(argv[1]):
        for s in Subfolder:
            for file in File:
                actualpath=os.path.join(Folder,file)
                hash=calculateCheckSum(actualpath)
                if hash in l:
                    f.write(hash)
                    f.write('\n')
                else:
                    l.append(hash)
                    



if __name__=="__main__":
    main()