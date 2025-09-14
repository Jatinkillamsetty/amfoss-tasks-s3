#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n, x, y;
        scanf("%d", &n);
        scanf("%d %d", &x, &y);

        int speed = (x < y) ? x : y;       
        int time = (n + speed - 1) / speed; 
        printf("%d\n", time);
    }

    return 0;
}
