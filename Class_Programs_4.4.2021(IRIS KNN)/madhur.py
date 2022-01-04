from mymodules import accuracy_score

def CalculateDistance(X,Y):
    return distance.euclidean(X,Y)



class KNN():
    def fit(self,training_data,training_target):
        print("Data Training done")
        self.training_data=training_data
        self.training_target=training_target
        #fit is like init function just used so that we can acccess all training data


    def predict(self,Test_data):
        predictions=[]
        for row in Test_data:
            label=self.Shortest(row)
            predictions.append(label)
        return predictions
        #here we create a list in which we add all our calculated results from testing

    #function shortest is used to find the distance between our test value and all the training data
    #and we find the shortest distance between them and use that for predicition
    #like we predict since it is nearer to the e.g setosa so it is setosa
    #we then add this to the row of out results i.e predictions list
    def Shortest(self,row):
        minIndex=0
        MinDistance=CalculateDistance(row,self.training_data[0])
    
        for i in range (1,len(self.training_data)):
            Distance=CalculateDistance(row,self.training_data[i])
            if Distance<MinDistance:
                MinDistance=Distance
                minIndex=i
        return self.training_target[minIndex]
        #here we use euclidean distance to find distance between 2 points
        #it is like we find the shortest distance that stores distances between our data and all of training data
        #and from we are finding  smallest or minimum value of the in MinDistance and store that index in minIndex and 
        #return that minIndex  i.e the answer 0,1,2 and that gets stored in predictions then we compare it at the end and find accuracy
        

    

def main():
    print("inside main")
    iris=load_iris()
    #loading data
    data=iris.data
    target=iris.target
    #dividing data into questions and answers sort of thing
    data_train,data_test,target_train,target_test=train_test_split(data,target,test_size=0.75)
    #cutting data into 4 parts that is train questions and train answers i.e features and labels
    #test_data and test_target i.e question and answers of data used for testing using split function
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
    #calling our class
    mobj.fit(data_train,target_train)
    #calling it's functions
    ret=mobj.predict(data_test)
    #getting results from the prediction function
    Accuracy=accuracy_score(target_test,ret)
    #calculating accuracy by inbuilt accuracy score by comparing our results i.e predictions list here
    #is referenced as ret and target_test is the one that has answers of the test

    count=0
    for i in range(len(data_test)):
        #print("ID:%d Expectation:%s Prediction:%s"%(i,target_test[i],ret[i]))
        if(ret[i]!=target_test[i]):count+=1
        #loop to compare data and find difference between our results and target_data
    #print(Line)
    print("no of differences between expectated values and tested values is:",count)
    print("Accuracy of KNN as calculated by us is: ",100-count,"%")
    print("Accuracy of KNN as calculated by accuracy_score is: ",Accuracy,"%")

if __name__=="__main__":
    main()