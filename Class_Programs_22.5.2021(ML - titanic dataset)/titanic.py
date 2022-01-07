import pandas as pd
from matplotlib.pyplot import figure,show
from seaborn import countplot

def titanic_logistic():
    #step 1(load data)
    titanic_data=pd.read_csv("main.csv")

    print("First five records of Dataset: ")
    print(titanic_data.head(5))
    print("Total number of records are:",len(titanic_data))

    #Step 2-(Analyse the data)
    print("Visualisation of survived and non-survived passengers")
    figure()
    countplot(data=titanic_data,x="Survived").set_title("Survived vs Dead")
    show()
    print("Visualization according to gender")
    figure()
    countplot(data=titanic_data,x="Survived",hue="Sex").set_title("Visualization according to sex")
    show()
    print("Visualisation according to class")
    figure()
    countplot(data=titanic_data,x="Survived",hue="Pclass").set_title("Supervised vs Unsupervised based on PClass")
    show()

def main():
    print("Titanic Dataset")
    titanic_logistic()
    
    





if __name__=="__main__":
    main()