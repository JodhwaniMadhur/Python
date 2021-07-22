import pandas as pd
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OrdinalEncoder,LabelEncoder

def Predictor(path):
    x=[1,2,3,4,5]
    y=[3,4,2,4,5]

    X_Mean=np.mean(x)
    Y_Mean=np.mean(y)

    Numerator,Denominator=0,0

    for i in range(len(x)):
        Numerator+=(x[i]-X_Mean)*(y[i]-Y_Mean)
        Denominator+=((x[i]-X_Mean)**2)


    m=Numerator/Denominator
    print("Values of X: ",x)
    print("Values of Y: ",y)
    print("valur of m: ",m)
    c=Y_Mean-(m*X_Mean)
    print("Value of c: ",c)
    sum1,sum2=0,0
    for i in range(len(x)):
        Y_predicted=m*x[i]+c
        sum1+=((Y_predicted-Y_Mean)**2)
        sum2+=((y[i]-Y_Mean)**2)


    print(sum1/sum2)


    #summation (Y_predicted-Y_mean)**2/(Y-Y_Mean)**2


    





def main():
    print("Play Predictor App")
    print("Enter file which contains dataset")
    path=input()
    Predictor(path)




if __name__=="__main__":
    main()