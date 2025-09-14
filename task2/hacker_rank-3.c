#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int k;
        int c = 0;
        int arr[100];
        scanf("%d", &k);
        for (int j = 0; j < k; j++) {
            scanf("%d", &arr[j]);
        }

        for (int y = 0; y < k; y++) {
            for (int z = y + 1; z < k; z++) {
                if (arr[z] < arr[y]) {
                    int temp = arr[y];
                    arr[y] = arr[z];
                    arr[z] = temp;
                }
            }
        }

        while ((arr[0] + arr[k - 1]) % 2 != 0) {
            int odd = 0, even = 0;
            for (int j = 0; j < k; j++) {
                if (arr[j] % 2) odd++;
                else even++;
            }

            if (odd < even) {
                if (arr[0] % 2) {
                    for (int j = 0; j < k - 1; j++) arr[j] = arr[j + 1];
                    k--;
                } else {
                    k--;
                }
            } else {
                if (arr[0] % 2 == 0) {
                    for (int j = 0; j < k - 1; j++) arr[j] = arr[j + 1];
                    k--;
                } else {
                    k--;
                }
            }
            c++;
        }

        printf("%d\n", c);
    }
}
