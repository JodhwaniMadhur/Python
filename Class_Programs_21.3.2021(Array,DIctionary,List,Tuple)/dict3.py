def main():
    employee={
    11:{"Name":"Piyush","Age":31},
    12:{"Name":"Madhur","Age":21},
    13:{"Name":"Sarvesh","Age":39},
    14:{"Name":"Amar","Age":21},
    15:{"Name":"Siddhi","Age":9}
    }
    print("Employee information is")
    for eid,einformation in employee.items():
        print("employee ID is:",eid)
        for key in einformation:
            print(key,einformation[key])
        print("------------------------------")



if __name__=="__main__":
    main()