import os
from sys import argv

def DirectoryTraversal(path):
    print("Contents of the Directory are: ")
    for Folder,SubFolder,Filename in os.walk(path):
        print("Directory name is: "+Folder)
    for _ in SubFolder:
        print("Subfolder of "+Folder +"is "+ SubFolder)
    for file in Filename:
        print("File name is:"+file)





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
    DirectoryTraversal(argv[1])


if __name__=="__main__":
    main()