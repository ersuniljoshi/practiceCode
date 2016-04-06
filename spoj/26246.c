#include <stdio.h>
#include <math.h>

long int arr[100] = {0};
int primeNumber(long int p)
{
    int i,root;
    root = sqrt(p);
    for(i=2;i<=root;i++)
    {
        if (p%i ==0)
            return 1;
    }
    return 0;
}

int main()
{
    long int b,sum;
    scanf("%ld",&b);
    for(i=0;i<num;i++)

    printf("%ld",sum);
    return 0;
}
