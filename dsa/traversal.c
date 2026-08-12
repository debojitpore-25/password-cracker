#include<stdio.h>
void main()
{
    int size,arr[20],i;


    printf("enter the size of the array: ");
    scanf("%d",&size);

    printf("enter the elements: ");

    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }

    printf("the entered elements in the array are :");

    for(i=0;i<size;i++)
    {
        printf(" %d",arr[i]);
    } 


}