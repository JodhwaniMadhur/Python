from os import path

def chkfile(str):
    return path.exists(str)

def main():
    string=input("Enter file name to be searched in the current directory")
    print(chkfile(string))

if __name__=="__main__":
    main()