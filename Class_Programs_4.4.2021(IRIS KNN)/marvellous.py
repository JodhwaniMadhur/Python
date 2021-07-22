from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
from sklearn.metrics import accuracy_score

def CalculateDistance(X,Y):
    return distance.euclidean(X,Y)
    
class Marvellous():
    def fit(self,TrainingData, TrainingTarget):
        print("Data Training Done")
        self.TrainingData = TrainingData
        self.TrainingTarget = TrainingTarget
        
    def predict(self,TestData):
        predictions = []
        for row in TestData:
            label = self.Shortest(row)
            predictions.append(label)
        return predictions
    
    def Shortest(self,row):
        Minindex = 0
        MinDistance = CalculateDistance(row,self.TrainingData[0])
        for i in range(1,len(self.TrainingData)):
            Distance = CalculateDistance(row,self.TrainingData[i])
            if Distance < MinDistance:
                MinDistance = Distance
                Minindex = i
        return self.TrainingTarget[Minindex]
        
def MarvellousKNN():
    print("Inside user defined KNN implelemntation..")
    iris = load_iris()
    
    data = iris.data
    target = iris.target
    
    data_train,data_test,target_train,target_test = train_test_split(data,target,test_size = 0.5)
    print("Data set loaded succesfully...")
    
    mobj = Marvellous()
    
    mobj.fit(data_train,target_train)
  
    ret = mobj.predict(data_test)
    Accuracy = accuracy_score(target_test,ret)
    return Accuracy
    
def main():
    ret = MarvellousKNN()
    print("Accuracy of KNN is : ",ret*100,"%")
    
if __name__ == "__main__":
    main()
