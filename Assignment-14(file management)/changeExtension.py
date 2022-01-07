import os
from sys import argv

def changextension(path,old_ext,new_ext):
    for _,subfolder,file in os.walk(path):
        for _ in subfolder:
            for f in file:
                if(os.path.splitext(f)[1]==old_ext):
                    os.rename(f,os.path.splitext(f)[0]+new_ext)


def main():
    changextension(argv[1],argv[2],argv[3])



if __name__=="__main__":
    main()