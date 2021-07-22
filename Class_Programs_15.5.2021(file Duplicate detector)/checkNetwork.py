from urllib.request import urlopen
try:
        urlopen('http://www.google.com', timeout=1)
        print("True")
except:
        print("False")

def is_internet_available():
    try:
        urlopen('http://www.google.com', timeout=1)
        return True
    except:
        return False