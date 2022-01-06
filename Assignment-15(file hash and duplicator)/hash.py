import hashlib
from sys import argv
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
    for Folder,Subfolder,File in os.walk(argv[1]):
        for s in Subfolder:
            for file in File:
                actualpath=os.path.join(Folder,file)
                print(calculateCheckSum(actualpath))


if __name__=="__main__":
    main()