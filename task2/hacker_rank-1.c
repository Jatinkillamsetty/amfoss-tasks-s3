#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int a,x,y;
        scanf("%d %d %d",&a,&x,&y);
        int dax=(a>x)?(a-x):(x-a);
        int day=(a>y)?(a-y):(y-a);
        int count=0;
        for (int j=1;j<=100;j++)
        {
            if (j!=a)
            {
                if (abs(j-x)<dax && abs(y-j)<day)
                {
                    count=1;
                    printf("YES \n");
                    break;
                }
                
            }
        }
        if (!count)
            printf("NO \n");
        
    }
}