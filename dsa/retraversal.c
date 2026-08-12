#include<stdio.h>
void main()
{
    int arr[20],size,i;

    printf("enter the size :");
    scanf("%d",&size);

    printf("enter the elements :");
    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }

    printf("the elements are :");
    for(i=0;i<size;i++)
    {
        printf(" %d ",arr[i]);
    }
}