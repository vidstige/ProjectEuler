#include <stdio.h>

int factor(int n, int *factors, size_t size) {
    int c = 0;
    while (n > 1) {
        for (int i = 2; i < n + 1; i++) {
            if (n % i == 0) {
                n /= i;
                factors[c++] = i;
                if (c >= size) {
                    // We filled the array 
                    printf("Oh shit\n");
                    return c;
                }
                break;
            }
        }
    }
    return c;
}

int main() {
    int factors[1024];
    int proper[1000001];
    long count = 0;

    for (int d = 2; d < 1000001; d++) {
        for (int i = 0; i < d; i++) {
            proper[i] = 1;
        }
        int fc = factor(d, factors, 1024);
        for (int i = 0; i < fc; i++) {
            for (int j = 0; j < d; j += factors[i]) {
                proper[j] = 0;
            }
        }
        for (int i = 0; i < d; i++) {
            if (proper[i]) {
                //printf("%d/%d\n", i, d);
                count++;
            }
        }
    }

    printf("%ld\n", count);
}
