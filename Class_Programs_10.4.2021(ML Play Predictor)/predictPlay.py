import pandas as pd
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OrdinalEncoder,LabelEncoder

def Predictor(path):
    data=pd.read_csv(path)
    
    #prepare data
    weather,Temprature,Play=data.Wether,data.Temperature,data.Play
    ordinal=LabelEncoder()
    w=ordinal.fit_transform(weather)
    t=ordinal.fit_transform(Temprature)
    p=ordinal.fit_transform(Play)

    print(w,t,p)
    obj=KNeighborsClassifier(n_neighbors=3)
    j=list(zip(w,t))
    obj.fit(j,p)
    print(obj.predict([[0,2]]))



def main():
    print("Play Predictor App")
    print("Enter file which contains dataset")
    path=input()
    Predictor(path)




if __name__=="__main__":
    main()