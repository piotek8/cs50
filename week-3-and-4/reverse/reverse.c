#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input);

    if (check_format(header) != 1)
    {
        printf("File is not a WAV file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open %s.\n", argv[2]);
        return 1;
    }

    fwrite(&header, sizeof(WAVHEADER), 1, output);

    int block_size = get_block_size(header);

    fseek(input, block_size, SEEK_END);

    while (ftell(input) - block_size > sizeof(header))
    {
        fseek(input, -2 * block_size, SEEK_CUR);
        BYTE c[block_size];
        fread(&c, block_size, 1, input);
        fwrite(&c, block_size, 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    char *format = "WAVE";
    for (int i = 0; i < 4; i++)
    {
        if (header.format[i] != format[i])
        {
            return 0;
        }
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    return header.numChannels * (header.bitsPerSample / 8);
}
