
def main():
    name=input("Enter the name that of file you want to create")
    fobj=open(name,"r")
    size=int(input("Enter number of bytes for reading"))
    print(fobj.read(size))

if __name__=="__main__":
    main()