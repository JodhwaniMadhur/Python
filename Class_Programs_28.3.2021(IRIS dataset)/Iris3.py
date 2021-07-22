from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
def main():
    dataset=load_iris()

    #print("Features of dataset ",dataset.feature_names)
   # print("Target names of dataset")
    #print(dataset.target_names)
    #for icnt in range(len(dataset.target)):
        #print("ID:%d Feature:%s Label:%s" %(icnt,dataset.data[icnt],dataset.target[icnt]))
    
    index=[1,5,2,4,56,51,101,99]
    test_target=dataset.target[index]
    test_feature=dataset.data[index]

    train_target=np.delete(dataset.target,index)
    train_feature=np.delete(dataset.data,index,axis=0)
    obj=tree.DecisionTreeClassifier()
    obj.fit(train_feature,train_target)
    result=obj.predict(test_feature)
    print("Result prediction by ML ",result)
    print("Result expected ",test_target)

if __name__=="__main__":
    main()