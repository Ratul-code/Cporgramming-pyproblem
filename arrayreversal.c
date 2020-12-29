#include <stdio.h>
void arrayreversal(int arr[]){
    int j=6;
    int temp;
    for (int i = 0; i <= 2;)
    {
        temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
        j--;
        i++;
    }
    
}
int main()
{
   int arra[7]={1,2,3,4,5,6,7};
   arrayreversal(arra);
   printf("[");
   for (int i = 0; i < 7; i++)
   {
       printf("%d",arra[i]);
   }
   printf("]");
   
//    printf("%d",arra);
    
    return 0;

}