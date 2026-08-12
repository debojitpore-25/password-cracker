#include<stdio.h>
void main()
{
    int arr[30],size,i;

    printf("enter the size of the array :");
    scanf("%d",&size);

    printf("enter the elements :");

    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }

    printf("the elemnts are :");
    for(i=0;i<size;i++)
    {
        printf("%d",arr[i]);
    }
}