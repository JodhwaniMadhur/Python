def SumDigits(num):
    sum_of_var=0
    while num>0:
        i=num%10
        sum_of_var=sum_of_var+i
        num=num//10
    print(sum_of_var)

no=int(input())
SumDigits(no)