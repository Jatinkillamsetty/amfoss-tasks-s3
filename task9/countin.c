#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char *fo = NULL;
    int number_lines = 0;
    int count_words = 0;
    int count_lett = 0;

    for (int i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-l") == 0)
            number_lines = 1;
        else if (strcmp(argv[i], "-w") == 0)
            count_words = 1;
        else if (strcmp(argv[i], "-c") == 0)
            count_lett = 1;
        else
            fo = argv[i];
    }

    if (fo == NULL)
    {
        fprintf(stderr, "No input file provided.\n");
        return 1;
    }

    FILE *fptr = fopen(fo, "r");
    if (fptr == NULL)
    {
        perror("Error opening file");
        return 1;
    }

    char info[1024];
    int line_num = 0;
    int word_count = 0;
    int total = 0;

    while (fgets(info, sizeof(info), fptr))
    {
        line_num++;

        int in_word = 0;
        for (int i = 0; info[i] != '\0'; i++)
        {
            if (isalpha(info[i]))
                total++;

            if (isspace(info[i]))
                in_word = 0;
            else if (!in_word)
            {
                in_word = 1;
                word_count++;
            }
        }
    }

    fclose(fptr);

    if (number_lines)
        printf("%d\n", line_num);
    if (count_words)
        printf("%d\n", word_count);
    if (count_lett)
        printf(" %d\n", total);

    return 0;
}
