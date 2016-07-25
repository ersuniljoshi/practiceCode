#include <stdio.h>

int G = 0;
void main()
{
    static int s = 0;
    int n;
    int *p;
    int *q;
    n = 5;
    p = &n;
    q = p;
}
