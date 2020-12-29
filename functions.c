#include <stdio.h>

void change(int a , int b){
    int temp = a;
    a=b;
    b=a;
}
// void change(int* a , int* b){
//     int temp =*a;
//     *a=*a + *b;
//     *b=temp - *b;
// }
int main()
{
    int a=45;
    int c=5;
    change(a,c);
    printf("%d and %d",a,c);
    return 0;

}