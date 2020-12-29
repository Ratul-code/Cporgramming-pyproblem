#include <stdio.h>
int factorial(int n){
    if(n==0 || n==1){
        printf("%d",n);
        return 1;
    }
    printf("%d * %d\n",n,n-1);
    return (n * factorial(n-1));
    
}

int main()
{
    printf("function running\n");
    int a;
    scanf("%d",&a);
    printf("%d",factorial(a));
    return 0;
}
