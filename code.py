#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SUBMISSIONS 1000
#define MAX_SOURCE_SIZE 10000

int max(int a, int b) {
    return (a > b) ? a : b;
}

int lcs(char *X, char *Y, int m, int n) {
    int L[m + 1][n + 1];
    int i, j;

    // Build L[m+1][n+1] in bottom-up fashion
    for (i = 0; i <= m; i++) {
        for (j = 0; j <= n; j++) {
            if (i == 0 || j == 0) {
                L[i][j] = 0;
            } else if (X[i - 1] == Y[j - 1]) {
                L[i][j] = L[i - 1][j - 1] + 1;
            } else {
                L[i][j] = max(L[i - 1][j], L[i][j - 1]);
            }
        }
    }
    return L[m][n];
}

int main() {
    char submissions[MAX_SUBMISSIONS][MAX_SOURCE_SIZE];
    int num_submissions = 0;

    // Read submissions from input
    while (fgets(submissions[num_submissions], MAX_SOURCE_SIZE, stdin) != NULL) {
        num_submissions++;
    }

    // Compare each pair of submissions
    int i, j;
    for (i = 0; i < num_submissions; i++) {
        for (j = i + 1; j < num_submissions; j++) {
            int lcs_len = lcs(submissions[i], submissions[j], strlen(submissions[i]), strlen(submissions[j]));
            double similarity = (double)lcs_len / max(strlen(submissions[i]), strlen(submissions[j]));

            printf("Similarity between submissions %d and %d: %f\n", i + 1, j + 1, similarity);
        }
    }

    return 0;
}
