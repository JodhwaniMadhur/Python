import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression




def predictor(train_x,train_y,test_x,test_y):
    obj=LinearRegression()
    obj.fit(train_x,train_y)
    print("R Square value is: ",obj.score(train_x,train_y))



def data_divider(data):
    length=len(data)
    train_size=int(0.8*length)
    test_size=length-train_size
    train_data=data.head(train_size)
    test_data=data.tail(test_size)
    return train_data,test_data

def data_converter(data):
    return data.astype(np.int64)

def main():
    path="Advertising.csv"
    data=pd.read_csv(path)
    print(data.info())
    attributes=['TV','radio','newspaper']
    data_label=data_converter(pd.read_csv(path,usecols=attributes))
    data_target=data_converter(pd.read_csv(path,usecols=['sales']))
    train_label,test_label=data_divider(data_label)


    train_target,test_target=data_divider(data_target)
    print(train_label.info())
    print(train_target.info())
    predictor(train_label,train_target,test_label,test_target)




if __name__=="__main__":
    main()