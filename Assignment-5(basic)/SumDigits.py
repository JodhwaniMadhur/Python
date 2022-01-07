sum=0
def Sum(value):
    global sum
    if value==0:
        print(sum)
    if value!=0:
        sum=sum+(value%10)
        value=value//10
        Sum(value)
        
no=int(input())
Sum(no)