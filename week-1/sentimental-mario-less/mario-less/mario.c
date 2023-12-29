//#include <cs50.h>
//#include <stdio.h>
//
//int main(void)
//{
//    int height;
//    do
//    {
//        height = get_int("Height: ");
//    }
//    while (1 > height || height > 8);
//
//    for (int i = 0; i < height; i++)
//    {
//        for (int j = 0; j < height - i - 1; j++)
//        {
//            printf(" ");
//        }
//
//        for (int k = 0; k < i + 1; k++)
//        {
//            printf("#");
//        }
//
//        printf("\n");
//    }
//
//    return 0;
//}


#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
    int hight = get_int("Enter the height of your pyramid: ");
    draw(hight);
}

void draw(int n)  //5
{
    for (int i = 0; i < n; i++)
    {// i=1
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
