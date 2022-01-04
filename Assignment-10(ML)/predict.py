from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def KNN(data_train,target_train,data_test):
    obj=KNeighborsClassifier(n_neighbors=1)
    obj.fit(data_train,target_train)
    return obj.predict(data_test)


def DTC(data_train,target_train,data_test):
    obj=tree.DecisionTreeClassifier()
    obj.fit(data_train,target_train)
    return obj.predict(data_test)

#Sunny 0
#Rainy 1
#Overcast 2

#Cool 0
#Hot 1
#mild 2

#No 1
#Yes 0
def main():
    questions=["Wether","Temperature"]
    answers=["Play"]
    data=pd.read_csv("train.csv")
    data_train=pd.read_csv("train.csv",usecols=questions)
    target_train=pd.read_csv("train.csv",usecols=answers)
    print("Training Data length is: ",len(data))
    data_test=pd.read_csv("test.csv",usecols=questions)
    target_test=pd.read_csv("test.csv",usecols=answers)
    print("Test data length is: ",len(data_test))
    ret1=DTC(data_train,target_train,data_test)
    ret2=KNN(data_train,target_train,data_test)
    print("Accuracy of KNN is: ",accuracy_score(target_test,ret2)*100)
    print("Accuracy of Tree is: ",accuracy_score(target_test,ret1)*100)


if __name__=="__main__":
    main()
