from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

def DecisionMaking():
    dataset=load_iris()
    # get dataset from iris and put it into dataset variable
    data=dataset.data
    #access data from dataset and initialize to data
    target=dataset.target
    #access data from dataset and initialize to data
    data_train,data_test,target_train,target_test=train_test_split(data,target,test_size=0.75)
    #declaring variables and  target_test takes output of train_test_split that splits
    #data in given ratio,here it is 0.75 and here it splits data and it's result into
    #75-25 parts and we train the model on 75% of the data and test on 25% data and they are assigned respectively to 
    #the given variables i.e 
    # data_train=75% of data for training
    # data_test=25% of data for testing
    # target_train=75% of data's answer for training
    # target_test=25% of data's answer for testing
    # we do not have to give the target_test for testing but here we store it for accuracy.

    tree_obj=tree.DecisionTreeClassifier()
    #declaring object of decision tree classifier
    tree_obj.fit(data_train,target_train)
    #giving the decision tree data for training and it's results

    output=tree_obj.predict(data_test)
    #testing the given data

    Accuracy=accuracy_score(target_test,output)
    #accuracy_score is sort of comparator and compares 
    # two lists here and we take the difference  of the output we already have 
    # and data we tested and it's results in accuracy
    return Accuracy


def main():
    ret=DecisionMaking()
    print("Accuracy of Decsion tree algorithm is: ",ret*100,"%")


if __name__=="__main__":
    main()