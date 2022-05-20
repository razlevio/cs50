#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    int quarters = 25;
    int quarterscount = 0;
    int dimes = 10;
    int dimescount = 0;
    int nickels = 5;
    int nickelscount = 0;
    int penny = 1;
    int pennycount = 0;
    int result = 0;
    float change;

    do
    {
        change = get_float("Change owed: ");
    }
    while (change < 0);
    
    int cents = round(change * 100);
    
    while ((cents - quarters) >= 0)
    {
        quarterscount++;
        cents = cents - quarters;
    }
    
    while ((cents - dimes) >= 0)
    {
        dimescount++;
        cents = cents - dimes;
    }
    
    while ((cents - nickels) >= 0)
    {
        nickelscount++;
        cents = cents - nickels;
    }
    
    while ((cents - penny) >= 0)
    {
        pennycount++;
        cents = cents - penny;
    }

    result = quarterscount + dimescount + nickelscount + pennycount;
    printf("%i\n", result);
}
