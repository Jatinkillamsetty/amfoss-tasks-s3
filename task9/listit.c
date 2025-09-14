#include<stdio.h>
#include<dirent.h>
#include<string.h>
#include<stdlib.h>

int main(int argc,char *argv[]){
    char *command=".";
    char *files[1000];
    int secret_file=0;
    int list_one=0;
    int reverse_file=0;

    for (int i=1;i<argc;i++)
    {
        if (strcmp(argv[i],"-a")==0)
            secret_file=1;
        else if (strcmp(argv[i],"-1")==0)
            list_one=1;
        else if (strcmp(argv[i],"-r")==0)
            reverse_file=1;
        else
            command=argv[i];
    }

    DIR *dir=opendir(command);
    if (dir == NULL) {
        perror("opendir failed");
        return 1;
    }

    struct dirent *entry;
    int filescount=0;

    while ((entry = readdir(dir)) != NULL)
        files[filescount++] = strdup(entry->d_name);
    closedir(dir);

    if (reverse_file) {
        for (int i = filescount-1; i >= 0; i--) {
            if (!secret_file && files[i][0] == '.') continue;
            printf("%s", files[i]);
            if (list_one) printf("\n"); else printf(" ");
            free(files[i]);
        }
    } else {
        for (int i = 0; i < filescount; i++) {
            if (!secret_file && files[i][0] == '.') 
            continue;
            printf("%s", files[i]);
            if (list_one) 
            printf("\n"); 
            else 
            printf(" ");
            free(files[i]);
        }
    }

    if (!list_one)
     printf("\n");
    return 0;
}
