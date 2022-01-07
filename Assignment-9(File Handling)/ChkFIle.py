from os import path

def chkfile(string):
    return path.exists(string)

def main():
    string=input("Enter file name to be searched in the current directory")
    print(chkfile(string))

if __name__=="__main__":
    main()