def main():
    batches={'PPA':12500,'LB':11000,'Python':13000,'Angular':10000}
    print("keys of dictionary")
    for value in batches.keys():
        print(value)

    print("keys and values of dictionary")
    for values in batches.keys():
        print(values,batches[values])

    print("keys and values are")
    for i,j in batches.items():
        print(i,j)

    batches["LSP"]=11000
    print(batches)
    print("ENTER NAME OF BATCH")
    name=input()
    print(batches.get(name))



if __name__=="__main__":
    main()