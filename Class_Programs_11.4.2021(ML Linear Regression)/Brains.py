import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def MeanData(column):
    return np.mean(column)


def headBrain(path):
    dataset=pd.read_csv(path)
    print("Size of dataset is: ",dataset.shape)
    print(dataset.describe())
    print(dataset.info())
    X=dataset["Head Size(cm^3)"].values
    Y=dataset["Brain Weight(grams)"].values
    print(len(X),len(Y))
    Mean_X=MeanData(X)
    Mean_Y=MeanData(Y)
    print("Value of Mean of X is: ",Mean_X)
    print("Value of Mean of Y is: ",Mean_Y)
    numerator,denominator=0,0
    for i in range(len(Y)):
        numerator+=(X[i]-Mean_X)*(Y[i]-Mean_Y)
        denominator+=(X[i]-Mean_X)**2

    m=numerator/denominator
    print("Value of slope is: ",m)
    c=Mean_Y-(m*Mean_X)
    print("Value of Y intercept is: ",c)
    X_start=np.min(X)-200
    X_end=np.max(X)+200
    x=np.linspace(X_start,X_end)
    y=m*x+c
    plt.plot(x,y,color='r',label="Regression Line")
    plt.scatter(X,Y,color='b',label="Scatter Plot")
    plt.xlabel("Head Size")
    plt.ylabel("Brain Weight")
    plt.legend()
    plt.show()

    sum1,sum2=0,0
    for i in range(len(x)):
        sum1+=(((m*X[i]+c)-Mean_Y)**2)
        sum2+=((Y[i]-Mean_Y)**2)
    print("Goodness of Fit is: ",sum1/sum2)
    
def main():
    print("Enter name of dataset")
    name="brain.csv"
    headBrain(name)

if __name__=="__main__":
    main()