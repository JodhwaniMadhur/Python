
def main():
    name=input("Enter the name that of file you want to create")
    fobj=open(name,"r")
    for Data in fobj:
        print(Data,end="")

if __name__=="__main__":
    main()