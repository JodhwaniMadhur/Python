import os
from sys import *

def changeExtension(path,old_ext,new_ext):
    for Folder,Subfolder,File in os.walk(path):
        for s in Subfolder:
            for f in File:
                if(os.path.splitext(f)[1]==old_ext):
                    os.rename(f,os.path.splitext(f)[0]+new_ext)


                    
                


def main():
    changeExtension(argv[1],argv[2],argv[3])



if __name__=="__main__":
    main()