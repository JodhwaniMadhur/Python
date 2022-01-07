def checkCount(file_content,word):
    return file_content.count(word)


def openAndCopy(str):
    fobj=open(str,"r")
    val=fobj.read()
    return val


def main():
    content=openAndCopy(input("Enter name of file: "))
    word=input("Enter the word to be searched: ")
    no=checkCount(content,word)
    print(no)

if __name__=="__main__":
    main()
