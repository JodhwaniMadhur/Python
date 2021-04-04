from sklearn import tree
def main():
    #Rough 1
    #Smooth 0
    #Tennis 1
    #Cricket 2

    #Step 1 & 2

    Features=[  [35,1],[47,1],[90,0],[48,1],
                [90,0],[35,1],[92,0],[35,1],
                [35,1],[35,1],[96,0],[43,1],
                [110,0],[35,1],[95,0]]

    Labels=[1,
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
    result=dobj.predict([[40,1]])
    print("Ball is",result)


if __name__=="__main__":
    main()