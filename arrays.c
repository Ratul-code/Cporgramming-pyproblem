// #include <stdio.h>

// int main()
// {
//     int marks[4] = {3,4,5,6};

//     for (int i = 0; i < marks[1]; i++)
//     {
//         printf("value of %d element is %d\n",i,marks[i]);
//     };
//     return 0;
#include <stdio.h>

int main()
{
    int marks[2][4]={{1,2,3,4},
                    {5,6,7,8}};

    for (int i = 0; i < marks[0][1]; i++)
    {
        for (int j = 0; j < marks[0][3]; j++)
        {
            printf("value of %d,%d element is %d\n",i,j,marks[i][j]);
        }
    };
    
    return 0;
}
