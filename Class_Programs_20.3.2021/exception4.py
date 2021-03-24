class AgeInvalid(Exception):
    def __init__(self,data):
        self.data=data

def main():
    age=int(input("Enter age for PAN card"))
    try:
        if age<18:
            raise AgeInvalid("Your age is less than 18")

    except AgeInvalid as obj:
        print(obj)

    else:
        print("You will get the PAN card within 7 buisness days")

if __name__=="__main__":
    main()