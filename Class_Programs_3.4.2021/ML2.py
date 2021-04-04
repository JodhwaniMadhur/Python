from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

def DecisionMaking(d,t):
    data1=d
    target1=t
    data_train,data_test,target_train,target_test=train_test_split(data1,target1,test_size=0.75)
    tree_obj=tree.DecisionTreeClassifier()
    tree_obj.fit(data_train,target_train)
    output=tree_obj.predict(data_test)
    Accuracy=accuracy_score(target_test,output)
    return Accuracy

def KNN(d,t):
    data2=d
    target2=t
    data_train,data_test,target_train,target_test=train_test_split(data2,target2,test_size=0.75)
    obj=KNeighborsClassifier()
    obj.fit(data_train,target_train)
    output=obj.predict(data_test)
    Accuracy=accuracy_score(target_test,output)
    return Accuracy

def main():
    dataset=load_iris()
    data=dataset.data
    target=dataset.target
    ret=DecisionMaking(data,target)
    print("Accuracy of Decsion tree algorithm is: ",ret*100,"%")
    ret=KNN(data,target)
    print("Accuracy of KNeighbors algorithm is: ",ret*100,"%")

if __name__=="__main__":
    main()