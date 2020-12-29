#include <stdio.h>
#include <string.h>
union hello
{
    char id[45];
};
int main()
{
    union hello s1;
    strcpy(s1.id,"harry");
    puts(s1.id);

    
    return 0;

}
