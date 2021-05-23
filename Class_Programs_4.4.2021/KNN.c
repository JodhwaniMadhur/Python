#include<stdio.h>
#include<math.h>

float distance(int x1, int y1, int x2, int y2)
{
    return sqrt(pow(x2 - x1, 2) +pow(y2 - y1, 2) * 1.0);
}

void KNNpredict(int label1[],int label2[],int target[],int test_data1[],int test_data2[],int train_len,int test_len)
{
    int index=0;
    int arr[test_len];
    for(int i=0;i<test_len;++i)
    {
        arr[index]=target[shortest(test_data1[i],test_data2[i],label1,label2,train_len)];
        index++;
    }
    for(int i=0;i<test_len;++i)
    {
        printf("%d\t",arr[i]);
    }
}

int shortest(int row1,int row2,int train1[],int train2[],int len)
{
    float minIndex=0;
    int minDistance=distance(row1,row2,train1[0],train2[0]);
    for(int i=1;i<len;++i)
    {
        int Distance=distance(row1,row2,train1[i],train2[i]);
        if(Distance<minDistance)
        {
            minDistance=Distance;
            minIndex=i;
        }
    }
    return minIndex;
}




int main()
{
    int label1[]={0, 0, 2, 1, 1, 1, 2, 0, 0, 1, 0, 2, 2, 1, 1, 1, 1, 2, 0, 0, 1, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 2, 1, 1, 1, 2, 0, 0, 1, 1};
    int label2[]={1, 1, 1, 2, 0, 0, 0, 2, 0, 2, 2, 2, 1, 2, 2, 0, 0, 0, 2, 0, 2, 2, 1, 1, 1, 2, 0, 0, 2, 0, 1, 1, 2, 0, 0, 0, 2, 0, 2, 0};
    int target[]={1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1};
    int train_len=40;
    int test1[]={0, 0, 2, 1, 1};
    int test2[]={1, 1, 1, 2, 0};
    int test_result[]={1, 1, 0, 1, 0};
    int test_len=5;

    KNNpredict(label1,label2,target,test1,test2,train_len,test_len);
    
}