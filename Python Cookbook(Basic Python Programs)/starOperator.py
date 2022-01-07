def drop_first_last(grades):
    _,*middle,_=grades
    #here middle with star considers to take whole list coz of assignment to the central list,
    # first gets assigned to the first  element and since middle has star it takes whole 
    # middle list and then last gets assigned to the last
    return sum_of_var(middle)/len(middle)

arr=[]
print("Enter number of elements in the list")
no=int(input())
i=0
while i < no:
    print("Enter value for element no:",i+1)
    arr.append(int(input()))
    i+=1

ans=drop_first_last(arr)
print(ans)