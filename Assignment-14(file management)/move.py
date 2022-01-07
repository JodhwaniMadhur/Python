import os
from sys import argv
import shutil
#Design automation script which accept two directory names. Copy all files from first directory
#into second directory. Second directory should be created at run time.



def main():
    src,dst=argv[1],argv[2]
    os.mkdir(str(dst))
    for _,Subfolder,_ in os.walk(argv[1]):
        for _ in Subfolder:
                shutil.copy(os.path.join(os.getcwd(),src),os.path.join(os.getcwd(),dst))


if __name__=="__main__":
    main()