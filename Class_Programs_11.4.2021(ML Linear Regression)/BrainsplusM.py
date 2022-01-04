import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression

def meandata(column):
    return np.mean(column)



def headbrain(path):
    dataset=pd.read_csv(path)
    print("Size of dataset is: ",dataset.shape)
    X=dataset["Head Size(cm^3)"].values
    Y=dataset["Brain Weight(grams)"].values
    X=X.reshape((-1,1))
    obj=LinearRegression()
    obj.fit(X,Y)
    
    #obj.predict((3613),(4747),(4423),(3804))
    #dataset=pd.read_csv(path)
    #X-new=dtaset["Head Size(cm^3)"].values
    #ouput=obj.predict(X_new)
    #print("Expected Result is: ",output)
    


    rsquare=obj.score(X,Y)
    print(rsquare)

    

    




def main():
    print("Enter name of dataset")
    name="brain.csv"
    headbrain(name)

if __name__=="__main__":
    main()