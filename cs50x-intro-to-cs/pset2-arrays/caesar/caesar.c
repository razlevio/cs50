#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
bool valid_key(string s);

int main(int argc, string argv[])
{
    if (argc != 2 || !valid_key(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext: ");
    int len = strlen(plaintext);
    printf("ciphertext: ");
    for (int i = 0; i < len; i++)
    {
        char c = plaintext[i];
        if (isalpha(c))
        {
            char m = 'A';
            if (islower(c))
            {
                m = 'a';
            }
            printf("%c", (c - m + key) % 26 + m);
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
}

bool valid_key(string s)
{
    int len = strlen(s);
    for (int i = 0; i < len; i++)
        if (!isdigit(s[i]))
        {
            return false;
        }
    return true;
}
