import os
from os import path

def ChkFile(str):
    return path.exists(str)

def main():
    string=input("Enter file name to be searched in the current directory")
    print(ChkFile(string))

if __name__=="__main__":
    main()