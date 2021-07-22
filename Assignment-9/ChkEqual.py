def ChkEqual(str1,str2):
    fobj1=open(str1,"r")
    fobj2=open(str2,"r")
    val1,val2=fobj1.read(),fobj2.read()
    return val1==val2

def main():
    name1=input("Enter the name of orignal file: ")
    name2=input("Enter the name of file to be checked: ")
    ans=ChkEqual(name1,name2)
    if ans==True:
        print("Content of both files are equal")
    else:
         print("Content of both files are not equal")

if __name__=="__main__":
    main()