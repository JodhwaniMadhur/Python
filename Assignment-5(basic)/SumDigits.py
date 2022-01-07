sum_of_var=0
def sum_of_var(value):
    global sum_of_var
    if value==0:
        print(sum_of_var)
    if value!=0:
        sum_of_var=sum_of_var+(value%10)
        value=value//10
        sum_of_var(value)
        
no=int(input())
sum_of_var(no)