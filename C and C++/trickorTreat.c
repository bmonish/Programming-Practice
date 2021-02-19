#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int searchForCandy(long long int x, long long int arr[], long int n)
{
    long int low = 0, high = n - 1, mid = (low + high) / 2;
    while (low <= high)
    {
        if (arr[mid] < x)
            low = mid + 1;
        else if (arr[mid] == x)
        {
            printf("Happy Halloween!\n");
            break;
        }
        else
            high = mid - 1;
        mid = (low + high) / 2;
    }
    if (low > high)
        printf("Tricky!\n");
    return 0;
}

int main()
{

    long int n, m;
    int i;

    // Getting N, A[N]
    scanf("%ld", &n);
    long long int A[n];
    for (i = 0; i < n; i++)
    {
        scanf("%lld", &A[i]);
    }

    // Getting M, C[M]
    scanf("%ld", &m);
    long long int C[m];
    for (i = 0; i < m; i++)
    {
        scanf("%lld", &C[i]);
        searchForCandy(C[i], A, n);
    }

    return 0;
}
