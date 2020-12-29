#include <stdio.h>
int fibn(int n){
    if(n==1){
        return 1;
    }
    else if(n==2){
        return 1;
    };
    return fibn(n-1) + fibn(n-2);
}
int hj(int n){
    int a=0;
    int b=1;
    int c;
   for (int i = 0; i < n; i++)
   {
       
       c=a+b;
       a=b;b=c;
   }
  return ("%d",a);
}
int main()
{
   printf("%d\n",hj(43));
//    printf("%d\n",fibn(43));
    return 0;
}
//0,1,1,2,3,5,8