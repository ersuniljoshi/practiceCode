#include <stdio.h>
#define STAR '*'
#define DOT '.'

int main()
{
    /* code */
    int t, r, c,i,j,k;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&r);
        scanf("%d",&c);
        for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
            {
                if (j%2 ==0 )
                {
                    if (k%2 == 0)
                        printf("%c",STAR);
                    else
                        printf("%c",DOT);
                }
                else
                {
                    if (k%2 == 0)
                        printf("%c",DOT);
                    else
                        printf("%c",STAR);
                }
            }
            printf("\n");
        }
        printf("\n");
    }

    return 0;
}
