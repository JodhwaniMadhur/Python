class C:
    def LearnAndCode(self):
        print("Learning C programming")

class CPP:
    def LearnAndCode(self):
        print("Learning C++ Programming")
    
class GoLang:
    def LearnAndCode(self):
        print("Learning GoLang Programming")

class Programmer:
    def Coding(self,language):
        language.LearnAndCode()

cobj=C()
cppobj=CPP()
gobj=GoLang()
obj=Programmer()
obj.Coding(cobj)
obj.Coding(cppobj)
obj.Coding(gobj)