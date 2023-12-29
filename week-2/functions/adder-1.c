#include <stdio.h>

int GetInt(void);
int add_two_ints(int a, int b);

int main(void)
{
    printf("Give me an integer: ");
    int x = GetInt();
    printf("Give me another integer: ");
    int y = GetInt();

    int z = add_two_ints(x,y);
    printf("The sum of %i and %i is %i!\n", x, y, z);
}

int GetInt(void)
{
    int input;
    scanf("%d", &input);
    return input;
}

int add_two_ints(int a, int b)
{
    int sum = a + b;
    return sum;
}

