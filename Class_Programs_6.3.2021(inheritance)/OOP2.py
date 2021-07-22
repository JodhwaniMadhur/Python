class Student:
    School="Abhinav"

    def __init__(self,no1,no2,no3):
        self.m1=no1
        self.m2=no2
        self.m3=no3

    def Instance_Total(self):
        print("inside instance method")
        return self.m1+self.m2+self.m3

    @classmethod
    def Class_DisplaySchool(cls):
        print("School name is:",cls.School)

    @staticmethod
    def Static_Info():
        print("The class contains information of school")

def main():
    Student.Class_DisplaySchool()#calling class method
    obj1=Student(50,80,70)#object creation
    obj2=Student(65,80,75)
    ret=obj1.Instance_Total()
    print("Total obtained marks",ret)
    Student.Static_Info() #calling static method


if __name__=="__main__":
    main()