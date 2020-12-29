#include <stdio.h>

int main()
{
    int age;
    scanf("%d", &age);
    printf("You have entered %d as your age\n",age);
    switch (age){
        case 3:
            printf("hello bara");
            break;
        default:
            printf("Nah bara");
            break;
    }
    return 0;
}
