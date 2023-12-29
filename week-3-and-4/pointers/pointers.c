#include <cs50.h>
#include <stdio.h>


int main(void)
{
    int a = 28;
    int b = 50;
    int *c = &a;

    *c = 14;
    c = &b;
    *c = 25;

    printf("a has the value %i, located at %p\n", a, &a); //14 , 0x700f245
    printf("b has the value %i, located at %p\n", b, &b); //25 , 0x700f123
    printf("c has the value %p, located at %p\n", c, &c); //0x700f123, 0x700def
}
       
