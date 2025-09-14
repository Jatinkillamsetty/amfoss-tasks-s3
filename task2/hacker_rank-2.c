#include <stdio.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        char s[15];  

        scanf("%d", &n);
        scanf("%s", s);

        int cones = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') 
                cones++;
        }

        int czeros = n - cones;

        int total = cones * (cones - 1) + czeros * (cones + 1);

        printf("%d\n", total);
    }

    return 0;
}