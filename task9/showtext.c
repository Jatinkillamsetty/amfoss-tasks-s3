#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char *fo = NULL;
    int number_lines = 0;
    int squeeze = 0;
    int show_end = 0;

    for (int i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-n") == 0)
            number_lines = 1;
        else if (strcmp(argv[i], "-s") == 0)
            squeeze = 1;
        else if (strcmp(argv[i], "-e") == 0)
            show_end = 1;
        else
            fo = argv[i];
    }

    if (fo == NULL)
    {
        fprintf(stderr, "Error: No file provided\n");
        return 1;
    }

    FILE *fptr = fopen(fo, "r");
    if (fptr == NULL)
    {
        perror("Error opening file");
        return 1;
    }

    char line[1024];
    int line_num = 0;
    int prev_blank = 0;

    while (fgets(line, sizeof(line), fptr))
    {
        int is_blank = (strcmp(line, "\n") == 0);

        if (squeeze && is_blank && prev_blank)
            continue;

        prev_blank = is_blank;

        line_num++;

        if (number_lines)
            printf("%6d  ", line_num);

        size_t len = strlen(line);
        if (show_end && len > 0 && line[len - 1] == '\n')
        {
            line[len - 1] = '\0';
            printf("%s$\n", line);
        }
        else
        {
            printf("%s", line);
        }
    }

    fclose(fptr);
    return 0;
}
