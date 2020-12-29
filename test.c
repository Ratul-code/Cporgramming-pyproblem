#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
    char ins[45]="hello boy";
    char inst[45];
    gets(inst);
    puts(inst);
    return 0;
}
// int arrs(int* arr){
//     printf("%d and %d\n",arr,&arr[1]);
// }
// int main()
// {
//     int arr[9]={1,2,3,4,5,6,7};
//     arrs(&arr);
//     printf("%d",&arr[1]);

//     return 0;
// }
// int main(){
//     int a=232792560;
//     int c=21;
//     int k=0;
//     while(1){
//         if(a%2520==0){
//             for (int i = 1; i <=c; i++)
//             {
//                 if(a%i==0){
//                     k++;
//                 } 
//             }
//                 if(k==c){
//                     printf("%d",a);
//                     break;
//                 }
//                 else{
//                     a=a+2520;
//                 }
//             k=0; 
//         }
//         else{
//             a++;
//         }
//     }    
//     return 0;
// }
// int main(){
//     int a=232792560;
//     int c=21;
//     int k=0;
//     while(1){
//         if(a%2520==0){
//             for (int i = 1; i <=c; i++)
//             {
//                 if(a%i==0){
//                     k++;
//                 } 
//             }
//                 if(k==c){
//                     printf("%d",a);
//                     break;
//                 }
//                 else{
//                     a=a+2520;
//                 }
//             k=0; 
//         }
//         else{
//             a++;
//         }
//     }    
//     return 0;
// }





// int main()
// {
//     int T,a,b;
//     scanf("%d\n",&T);
//     for (int i = 0; i <= T; i++)
//     {
//         scanf("%d %d",&a,&b);
//         printf("%d",a+b);
//     }
//     return 0;
// }
// int main()
// {
//     int a;
//     float b;
//     float c=0.50;
//     scanf("%d %f",&a,&b);
//     if((a+c)<b & a%5==0){
//         b=b-(a+c);
//         printf("%f",b);
//     }
//     else{
//         printf("%f",b);
//     }
//     return 0;
// }





// int main() {
// 	// Read the input n, k
// 	int n, k,i;
	
// 	scanf("%d %d\n", &n, &k);
	

// 	// ans denotes number of integers n divisible by k
// 	int count = 0;

// 	for(i=0;i<n;i++)
// 	{
// 	    int num;
// 	    scanf("%d",&num);
// 	    if(num%k==0){
// 	        count++;
// 	    }
// 	}

// 	// Print the count.
// 	printf("%d\n", count);
	
// 	return 0;
// }
// int main() 
// {
// 	int a,b,c,i,d;
//     scanf("%d",&a);
//     for ( i = 0; i < a; i++)
//     {
//         scanf("%d",&b);
//         printf("%d",b);
//         d=1;
//         for ( c = 1; c <= b;)
//         {
//             d=d*c;
//             c++;
//             printf("%d",d);
//         }
//         printf("%d\n",d);
        
//     }
    
// 	return 0;
// }

// #include <stdio.h>
/*
You manage a travel agency and you want your n drivers to input their following details:
1. Name
2. Driving License No
3. Route 
4. Kms
Your program should be able to take n as input(or you can take n=3 for simplicity) and your drivers will start inputting their details one by one.

Your program should print details of the drivers in a beautiful fashion.
User structures.
*/
