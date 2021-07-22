from googlesearch import search

class Gsearch_python:
    def __init__(self,name_search):
        self.name = name_search

    def Gsearch(self):
        count = 0
        for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=1,pause=2):
                count += 1
                print (count)
                print(i + '\n')

if __name__=='__main__':
    gs = Gsearch_python("Tutorialspoint Python")
    gs.Gsearch()
