
def main():
    name=input("Enter the name that of file you want to create")
    fobj=open(name,"r")
    print(fobj.read())

if __name__=="__main__":
    main()