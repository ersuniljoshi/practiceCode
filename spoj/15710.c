#include <stdio.h>

int main()
{
    long int a,b,sum;
    scanf("%ld",&a);
    scanf("%ld",&b);
    sum =0;
    while(a<=b)
    {
        sum += a*a;
        a++;
    }

    printf("%ld",sum);
    return 0;
}
