import numpy as np 

def predictor(path):
    x=[1,2,3,4,5]
    y=[3,4,2,4,5]

    x_mean=np.mean(x)
    y_mean=np.mean(y)

    numerator,denominator=0,0

    for i in range(len(x)):
        numerator+=(x[i]-x_mean)*(y[i]-y_mean)
        denominator+=((x[i]-x_mean)**2)


    m=numerator/denominator
    print("Values of X: ",x)
    print("Values of Y: ",y)
    print("valur of m: ",m)
    c=y_mean-(m*x_mean)
    print("Value of c: ",c)
    sum1,sum2=0,0
    for i in range(len(x)):
        y_predicted=m*x[i]+c
        sum1+=((y_predicted-y_mean)**2)
        sum2+=((y[i]-y_mean)**2)


    print(sum1/sum2)


    #summation (Y_predicted-Y_mean)**2/(Y-y_mean)**2


def main():
    print("Play Predictor App")
    print("Enter file which contains dataset")
    path=input()
    predictor(path)




if __name__=="__main__":
    main()