#include <stdio.h>

int main()
{
    printf("kms to metre - 1\ninches to meter - 2\npounds to kgs - 3");
    int d;
    scanf("%d",&d);
    // float a;
    // float b;
    // float c;
switch(d){
    float a;
    float b;
    float c;
    case 1:
        printf("Enter a distance in Kilometre\n");
        scanf("%f",&d);
        printf("In metre it is %f",d*1000);
        break;
    case 2:
        printf("Enter a length in Inches\n");
        scanf("%f",&b);
        printf("In metre it is %f",b*0.0254);
        break;
    case 3:
        printf("Enter a mass in pounds\n");
        scanf("%f",&c);
        printf("In metre it is %f",c*0.453592);
        break;
    default:
        printf("Enter a valid number please");
};
    return 0;
}
