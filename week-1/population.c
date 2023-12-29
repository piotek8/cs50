#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start, end;
    // Prompt for start size
    do
    {
        printf("Start size: ");
        scanf("%d", &start);
    }
    while (start < 9);

    // Prompt for end size
    do
    {
        printf("End size: ");
        scanf("%d", &end);
    }
    while (end < start);

    int years = 0;
    // Calculate number of years until we reach threshold
    while (start < end)
    {
        start += start / 3 - start / 4;
        years++;
    }
    // Print number of years
    printf("Years: %d\n", years);

    return 0;
}
