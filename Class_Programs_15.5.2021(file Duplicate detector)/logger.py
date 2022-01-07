
import os
from sys import argv

filepath=os.getcwd()


def Writer(dictionary,current_date_time):
    filename=os.path.join(filepath,current_date_time)
    f=open(filename, 'w') 
    for key, value in dictionary.items(): 
        f.write('%s:%s\n' % (key, value))
    f.close()

def DupWriter(lister):
    filename=os.path.join(filepath,"duplicates.txt")
    f=open(filename, 'w') 
    for value in lister.items(): 
        f.write('%s\n' % ( value))
    f.close()