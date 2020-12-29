#include <stdio.h>
#include <string.h>
// <h1>This is a heading</h1>
char parser(char string[]){
   int j=0;
   int x;
   for (int i = 0; i < strlen(string); i++)
   {
       if(string[i]=='<'){
           x=1;
        //    contin ue;
       }
       else if(string[i]=='>'){
           x=0;
           continue;
       }
       if(x==0){
           string[j]=string[i];
           j++;
       }
   }
   string[j]='\0';
   while(string[0]==' ')
   {
       for (int i = 0; i < strlen(string); i++)
       {
           string[i]=string[i+1];
       }    
   }
   while (string[strlen(string)-1]==' ')
   {
      string[strlen(string)-1]='\0';
       
   }   
}
int main()
{
    char str[]="<h1>hello</h1>";
    parser(str);
    printf("%s",str);
    
    return 0;

}