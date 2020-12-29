#include <stdio.h>
struct student
{
    int id;
    float marks;
} s1,s2,s3,s4;

int main()
{
    struct student s1 = {12,23.45};
    struct student s2 = {125,273};
    printf("%d\n",s1.id);
    printf("%f\n",s2.marks);
    printf("%d\n",s2.id);
    printf("%d\n",s1.id);
    printf("%d\n",s1.id);
    printf("%f\n",s1.marks);

    return 0;

}