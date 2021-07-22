import os
from sys import *

def fileExtensionChecker(path,ext):
    l=[]
    for Folder,SubFolder,File in os.walk(path):
        for sub in SubFolder:
            for file in File:
                split_tup=os.path.splitext(file)
                if((split_tup[1]==ext) and (file not in l)):
                    l.append(file)
    return l





def main():
    ret=fileExtensionChecker(argv[1],argv[2])
    for i in range(0,len(ret)):
        print(ret[i])


if __name__=="__main__":
    main()