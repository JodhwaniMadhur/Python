import os
from sys import *
import hashlib 
import checksum,logger,mailer,checkNetwork,twiliooo
from datetime import *
import time


def DirectoryTraversal(path):
    a_dict={}
    #print("Contents of the Directory are: ")
    for Folder,SubFolder,Filename in os.walk(path):
        for sub in SubFolder:
            ...
        for file in Filename:
            actualpath=os.path.join(Folder,file)
            hash=checksum.calculateCheckSum(actualpath)
            if hash in a_dict:
                a_dict[hash].append(actualpath)
            else:
                a_dict[hash]=[file]
    current_date_time=datetime.now().strftime("%d_%m_%Y-%I_%M")+".txt"
    logger.Writer(a_dict,current_date_time)
    ans=DisplayDuplicate(a_dict)
    mailer.mail(current_date_time,ans)
    twiliooo.tw(current_date_time,ans)
    
        
        

def DisplayDuplicate(a_dict):
    output = list(filter(lambda x : len(x) > 1, a_dict.values()))

    if(len(output) > 0):
        print("There are duplicate files")
    else:
        print("There are no dupicate files")
        return
    
    print("List of duplicate files are : ")
    icnt = 0
    counter=0
    for result in output:
        for path in result:
            icnt+=1
            if icnt >=2:
                os.remove(path)
                counter+=1
        icnt = 0
    return counter

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
    path=os.path.join(os.getcwd(),argv[1])
    if((os.path.isdir(path)==True) and (checkNetwork.is_internet_available()==True)):
        DirectoryTraversal(argv[1])




    

if __name__=="__main__":
    main()