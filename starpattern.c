#include <stdio.h>


int main()
{
    int a;
    printf("Enter 1 to serial wise Display\nEnter 2 to backward serial way Display\n");
    scanf("%d",&a);
    switch(a){
    int c;
    case 1:
        printf("How many row do you want?\n");
        scanf("%d",&c);
        for (int i = 0; i <= c; i++)
        {
            for (int j = 0; j < i; j++)
            {
                printf("%c",'*');
            }
            printf("\n");
        }
        break;
    case 2:
        printf("How many row do you want?\n");
         scanf("%d",&c);
        for (int i = c; i>0; i--)
        {
            for (int j = 0; j < i; j++)
            {
                printf("%c",'*');
            }
            printf("\n");
        }
        break;
    default:
        printf("you bitch");
        printf("%d",&a);
    }
    printf("%d",sizeof(4)+1);
    
    return 0;

}