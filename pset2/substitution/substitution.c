#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
bool valid_key(string s);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    
    if(!valid_key(argv[1]))
    {
        printf("Key must contain 26 characters and none same characters.\n");
        return 1;
    }
    
    string plaintext = get_string("Plaintext: ");
    string key = argv[1]; 
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string alphabet2 = "abcdefghijklmnopqrstuvwxyz";
    int plaintextlen = strlen(plaintext);
    
    char array[plaintextlen];
    for (int i = 0; i < plaintextlen; i++)
    {
        if(!isalpha(plaintext[i]))
        {
            array[i] = plaintext[i];
        }
        if (islower(plaintext[i]) > 0)
        {
            for (int j = 0; j < 26; j++)
            {
                if (plaintext[i] == alphabet2[j])
                {
                    array[i] = tolower(key[j]);
                }
            }
        }
        else
        {
            for (int j = 0; j < 26; j++)
            {
                if(plaintext[i] == alphabet[j])
                {
                    array[i] = toupper(key[j]);
                }
            }
        }
    }
    printf("ciphertext: ");
    for (int i = 0; i < plaintextlen; i++)
    {
        printf("%c", array[i]);
    }
    printf("\n");
}

bool valid_key(string s)
{
    int len = strlen(s);
    if (len != 26)
    {
        return false;
    }
    
    int freq[26] = { 0 };
    
    for (int i = 0; i < len; i++)
    {
        if(isalpha(s[i]) == 0)
        {
            return false;
        }
        
        int index = toupper(s[i]) - 'A';
        if (freq[index] > 0)
        {
            return false;
        }
        freq[index]++;
    }
    return true;
}
