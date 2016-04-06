#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[]) {
    int t,i,j,half;
    char str[200];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%s",&str);
        half = strlen(str)/2;
        for(j=0;j<half;j=j+2)
            printf("%c",str[j]);
        printf("\n");
    }
    return 0;
}
