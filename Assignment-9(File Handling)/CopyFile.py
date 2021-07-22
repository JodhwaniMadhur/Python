import sys

def main():
    val=Copy(sys.argv[1])
    Creat("Demo.txt",val)

def Creat(str1,w):
    fobj=open(str1,"w")
    fobj.write(w)

def Copy(str2):
    fobj=open(str2,"r")
    return fobj.read()


if __name__=="__main__":
    main()