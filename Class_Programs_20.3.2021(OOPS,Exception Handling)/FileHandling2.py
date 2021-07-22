
def main():
    name=input("Enter the name that of file you want to create")
    fobj=open(name,"w")
    str=input("Enter data for file writing")
    fobj.write(str)

if __name__=="__main__":
    main()