from mymodules import *

def CalculateDistance(X,Y):
    return distance.euclidean(X,Y)



class KNN():
    def fit(self,training_data,training_target):
        print("Data Training done")
        self.training_data=training_data
        self.training_target=training_target

    def predict(self,Test_data):
        predictions=[]
        for row in Test_data:
            label=self.Shortest(row)
            predictions.append(label)
        return predictions

    def Shortest(self,row):
        minIndex=0
        MinDistance=CalculateDistance(row,self.training_data[0])

        for i in range (1,len(self.training_data)):
            Distance=CalculateDistance(row,self.training_data[i])
            if Distance<MinDistance:
                MinDistance=Distance
                minIndex=i
        return self.training_target[minIndex]


    

def main():
    print("inside main")
    iris=load_iris()
    data=iris.data
    target=iris.target
    data_train,data_test,target_train,target_test=train_test_split(data,target,test_size=0.75)
    print("Data set loaded succesfully")
    #Line='*'*100

    #print(Line)
    #for i in range(len(iris.target)):
    #    print("ID: %d  Lable:%s ,Feature:%s" %(i,iris.data[i],iris.target[i]))
    #print(Line)
    #for i in range(len(data_train)):
    #    print("ID:%d Label:%s ,Feature:%s"%(i,data_train[i],target_train[i]))
    #print(Line)
    #for i in range(len(data_test)):
    #    print("ID:%d Label:%s ,Feature:%s"%(i,data_test[i],target_test[i]))
    #print(Line)

    
    mobj=KNN()
    mobj.fit(data_train,target_train)
    ret=mobj.predict(data_test)
    Accuracy=accuracy_score(target_test,ret)
    count=0
    for i in range(len(data_test)):
        #print("ID:%d Expectation:%s Prediction:%s"%(i,target_test[i],ret[i]))
        if(ret[i]!=target_test[i]):count+=1
    #print(Line)
    print("no of differences between expectated values and tested values is:",count)
    print("Accuracy of KNN is: ",100-count,"%")

if __name__=="__main__":
    main()