import pandas as pd
def main():
    iris = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    c=pd.read_csv(iris)
    print(c)
    



if __name__=="__main__":
    main()