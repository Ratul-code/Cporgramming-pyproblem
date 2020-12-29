#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    // int* ptr;
    // ptr =(int*)malloc(10*sizeof(int));
    // for (int i = 0; i < 4; i++)
    // {
    //     printf("Enter the elemnet of the array %d\n",i);
    //     scanf("%d",&ptr[i]);
    // }

    // for (int i = 0; i < 4; i++)
    // {
    //     printf("THe value of array %d\n",ptr[i]); 
    // }
    int* ptr;
    ptr =(int*)calloc(10,sizeof(int));
    for (int i = 0; i < 4; i++)
    {
        printf("Enter the elemnet of the array %d\n",i);
        scanf("%d",&ptr[i]);
    }

    for (int i = 0; i < 3; i++)
    {
        printf("THe value of array %d\n",ptr[i]); 
    }


// realloc
    ptr =(int*)realloc(ptr,10*sizeof(int));
    for (int i = 0; i < 10; i++)
    {
        printf("Enter the elemnet of the array %d\n",i);
        scanf("%d",&ptr[i]);
    }

    for (int i = 0; i < 10; i++)
    {
        printf("THe value of array %d\n",ptr[i]); 
    }
    free(ptr);
    printf("%d",ptr[1]);
    return 0;

}