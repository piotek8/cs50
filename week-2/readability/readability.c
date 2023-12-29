#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string string = get_string("What is the string to analyze? \n");

    int letters = 0;
    int words = 0;
    int sentences = 0;

    for (int i = 0, stringLength = strlen(string); i < stringLength + 1; i++)
    {
        if ((string[i] >= 'a' && string[i] <= 'z') || (string[i] >= 'A' && string[i] <= 'Z'))
        {
            letters++;
        }
        if (string[i] == ' ' || string[i] == '\0')
        {
            words++;
        }
        if (string[i] == '!' || string[i] == '.' || string[i] == '?')
        {
            sentences++;
        }
    }

    float averageWordsPer100 = (100 / (float) words) * (float) letters;
    float averageSentencePer100 = (100 / (float) words) * (float) sentences;
    int readingIndex = round(0.0588 * averageWordsPer100 - 0.296 * averageSentencePer100 - 15.8);

    if (readingIndex < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (readingIndex > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", readingIndex);
    }

    return 0;
}
