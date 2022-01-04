class BookStore:
    no=0
    def __init__(self,bookname,author):
        """
        Just initialization of variables is taking place here.
        """
        self.book=bookname
        self.name=author
        BookStore.no+=1
        
    def display(self):
        print(self.book,end=" ")
        print(self.name,end=" ")
        print("No. of books:",self.no)

def main():
    obj1=BookStore("Linux System Programming","Robert J Love")
    obj1.display()
    obj2=BookStore("C Programming","Dennis Ritchie")
    obj2.display()
    
if __name__=="__main__":
    main()