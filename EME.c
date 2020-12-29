#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    int*ptr;
    char in;
    int n,m;
    // scanf("%d",&m);
    scanf("%d",&n);
    ptr=(int*)calloc(n+1,sizeof(char));
    getchar();
    gets(ptr);
    // scanf("%s",ptr);
    // for (int i = 0; i < n+1; i++)
    // {
    //     scanf("%c",&in);
    //     ptr[i]=in;
    // }
    // for (int i = 0; i < n; i++)
    // {
    //     printf("%c",ptr[i]);
    // }
    // printf("%s",ptr);
    puts(ptr);
    free(ptr);
    return 0;

}