#include <cs50.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Wrong usage: Try. ./create [filename]\n");
        return 1;
    }
    int filename_length = strlen(argv[1]);

    char *filename = malloc(sizeof(char) * filename_length);

    sprintf(filename, "%s", argv[1]);

    FILE *new_file = fopen(filename, "w");
    if (new_file == NULL)
    {
        printf("Could not create file.\n");
        return 1;
    }

    fclose(new_file);

    free(filename);
}
