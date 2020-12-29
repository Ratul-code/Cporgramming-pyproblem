#include <stdio.h>

int array[1000001];

int main(){
  int i,j;
  scanf("%d",&j);
  int x;

  for (i=0;i<j;i++){
    scanf("%d",&x);

    array[x]=array[x]+1;      
  }    
  for (i=0;i<1000001;i++){
    while(array[i]>0){
      printf("h%d\n",i);
      array[i]--;
    }
  }

return 0;
}