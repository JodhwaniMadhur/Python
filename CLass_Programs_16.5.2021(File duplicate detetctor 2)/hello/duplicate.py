#https://us02web.zoom.us/j/81908539306?pwd=RlFVRlVTVVQ0ZkxoTE96Lzl3dnNNQT09


import os
from sys import *






def main():
    print("Directory Traversal Script")
    if(len(argv)!=2):
        print("Error:Invalid number of arguments")
        exit()
    if((argv[1]=="-h")or(argv[1]=="-H")):
        print("It is a Directory Cleaner Script")
        exit()
    if((argv[1]=="-u")or(argv[1]=="-U")):
        print("Usage:Provide absolute path of the target directory")
        exit()
    


if __name__=="__main__":
    main()