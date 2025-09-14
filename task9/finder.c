#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int number_lines = 0;
    int invert_match = 0;
    int count_flag = 0;
    char *pattern = NULL;
    char *filename = NULL;

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-n") == 0) {
            number_lines = 1;
        } else if (strcmp(argv[i], "-v") == 0) {
            invert_match = 1;
        } else if (strcmp(argv[i], "-c") == 0) {
            count_flag = 1;
        } else if (pattern == NULL) {
            pattern = argv[i];
        } else {
            filename = argv[i];
        }
    }

    if (pattern == NULL || filename == NULL) {
        fprintf(stderr, "Usage: %s [options] pattern file\n", argv[0]);
        return 1;
    }

    FILE *fptr = fopen(filename, "r");
    if (fptr == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[1024];
    int line_num = 0;
    int match_count = 0;

    while (fgets(line, sizeof(line), fptr)) {
        line_num++;
        int match = (strstr(line, pattern) != NULL);
        if (invert_match) match = !match;
        if (match) {
            match_count++;
            if (!count_flag) {
                if (number_lines)
                    printf("%d:%s", line_num, line);
                else
                    printf("%s", line);
            }
        }
    }

    if (count_flag) {
        printf("%d\n", match_count);
    }

    fclose(fptr);
    return 0;
}
