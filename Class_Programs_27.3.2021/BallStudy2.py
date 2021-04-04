from sklearn import tree

def MarvellousML(weight,surface):
    #Rough 1
    #Smooth 0
    #Tennis 1
    #Cricket 2

    #Step 1 & 2
    Features=[  [35,1],[47,1],[90,0],[48,1],
                [90,0],[35,1],[92,0],[35,1],
                [35,1],[35,1],[96,0],[43,1],
                [110,0],[35,1],[95,0]]

    Labels=[
    1,
    1,
    2,
    1,
    2,
    1,
    2,
    1,
    1,
    1,
    2,
    1,
    2,
    1,
    2,
    ]

    #step 3
    dobj=tree.DecisionTreeClassifier()

    #step 4
    dobj.fit(Features,Labels)

    #step 5
    result=dobj.predict([[weight,surface]])
    if result==1:
        print("Object looks like Tennis Ball")
    elif result==2:
        print("Object looks like Cricket Ball")
    else:
        print("Cannot identify object")
    


def main():
    print("Enter Weight of object")
    i=int(input())
    print("Enter number for Surface Type")
    j=input()
    if j=="rough":
        j=1
    if j=="smooth":
        j=0
    MarvellousML(i,j)


    


if __name__=="__main__":
    main()