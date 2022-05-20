#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int letters(int length, string text);
int words(int length, string text);
int sentences(int length, string text);

int main(void)
{
    string text = get_string("Text: ");
    int tlength = strlen(text);

    float index = 0;
    float L = 0;
    float S = 0;
    float lettersnum = letters(tlength, text);
    float wordsnum = words(tlength, text);
    float sentencesnum = sentences(tlength, text);

    //printf("%i letter(s)\n", (int) lettersnum); //Printing number of letters in the text
    //printf("%i word(s)\n", (int) wordsnum); //Printing number of words in the text
    //printf("%i sentence(s)\n", (int) sentencesnum); //Printing number of sentences in the text

    L = (lettersnum / wordsnum) * 100;
    S = (sentencesnum / wordsnum) * 100;
    index = (0.0588 * L) - (0.296 * S) - 15.8;
    if (index >= 1 && index < 16)
    {
        printf("Grade %i\n", (int)round(index));
    }
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
}

int letters(int length, string text)
{
    int count = 0;
    for (int i = 0; i < length; i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            count++;
        }
    }
    return count;
}

int words(int length, string text)
{
    int count = 1;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == ' ')
        {
            count++;
        }
    }
    return count;
}

int sentences(int length, string text)
{
    int count = 0;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}
