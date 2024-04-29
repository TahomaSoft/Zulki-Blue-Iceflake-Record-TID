#include <stdio.h>
 
int main()
{
    long decnum, quo, rem;
    int i, j = 0;
    char hexnum[100];
 
    printf("Enter decimal number: ");
    scanf("%ld", &decnum);
 
    quo = decnum;
 
    while (quo != 0)
    {
        rem = quo % 16;
        if (rem < 10)
            hexnum[j++] = 48 + rem;
        else
            hexnum[j++] = 55 + rem;
        quo = quo / 16;
    }
 
    
    for (i = j; i >= 0; i--)
            printf("%c", hexnum[i]);
    return 0;
}
