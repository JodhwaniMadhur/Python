class Arithmetic:
    #self here is like this keyword in java
    #callback constructor like
    #calls itself
    def __init__(self):
        """Just print statement here"""
        print("Inside Constructor")

def main():
    obj=Arithmetic()
    print(obj)
    
    

if __name__=="__main__":
    main()