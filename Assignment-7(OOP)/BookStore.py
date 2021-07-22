class BookStore:
    no=0
    def __init__(self,bookname,author):
        self.book=bookname
        self.name=author
        BookStore.no+=1
    def Display(self):
        print(self.book,end=" ")
        print(self.name,end=" ")
        print("No. of books:",self.no)

def main():
    obj1=BookStore("Linux System Programming","Robert J Love")
    obj1.Display()
    obj2=BookStore("C Programming","Dennis Ritchie")
    obj2.Display()
    
if __name__=="__main__":
    main()