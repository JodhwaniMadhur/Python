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
    l=[]
    f=open("log.txt","wt")
    for Folder,Subfolder,File in os.walk(argv[1]):
        for _ in Subfolder:
            for file in File:
                actualpath=os.path.join(Folder,file)
                hash_of_file=calculateCheckSum(actualpath)
                if hash_of_file in l:
                    f.write(actualpath)
                    f.write('\n')
                    os.remove(actualpath)
                else:
                    l.append(hash_of_file)



if __name__=="__main__":
    main()