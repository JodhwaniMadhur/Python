from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics


def SVM():
    cancer=datasets.load_breast_cancer()
    print("Features of dataset are: ",cancer.feature_names)

    print("Target of dataset are: ",cancer.target_names)

    print("shape of dataset is: ",cancer.data.shape)

    print("First five records are: ")
    print(cancer.data[0:5])

    print("Target of dataset is :",cancer.target)
    X_train,X_test,Y_train,Y_test=train_test_split(cancer.data,cancer.target,train_size=0.9,random_state=42)

    clf=svm.SVC(kernel='linear')

    clf.fit(X_train,Y_train)

    Y_pred=clf.predict(X_test)

    print("Accuracy of model is: ",metrics.accuracy_score(Y_test,Y_pred)*100)



def main():
    SVM()



if __name__=="__main__":
    main()