// Implements a dictionary's functionality

#include <stdbool.h>
#include "dictionary.h"
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// initialise positive hash value using unsigned int 
unsigned int hash_value;

// initialise (positive) hash table word count 
unsigned int word_count;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    //hash the word to get hash value
    hash_value = hash(word);

    //access the linked list  
    node *cursor = table[hash_value];

    //go through the linked list
    while (cursor != NULL)
    {
        //check if the word matches
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }

        //move cursor to next node
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;
    while ((c = toupper(*word++)))
    {
        hash = ((hash << 5) + hash) + c;
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dict 
    FILE *file = fopen(dictionary, "r");

    // If file is not opened, return false
    if (file == NULL)
    {
        return false;
    }

    // storage space for word
    char word[LENGTH + 1];

    // Scan dict for strings that are not the end of the file
    while (fscanf(file, "%s", word) != EOF)
    {
        // Allocate memory for new node
        node *n = malloc(sizeof(node));

        // If malloc returns NULL, return false
        if (n == NULL)
        {
            return false;
        }

        // Pointer to next node and word itself
        strcpy(n->word, word);

        // Hash the word to get hash value
        hash_value = hash(word);

        // Set new pointer
        n->next = table[hash_value];

        // Set head to new pointer
        table[hash_value] = n;

        word_count++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Check if there are any words
    if (word_count > 0)
    {
        // Return count
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Iterate through buckets
    for (int i = 0; i < N; i++)
    {
        // Set cursor to this each bucket location  
        node *cursor = table[i];
        
        // If cursor is not NULL, free  
        while (cursor)
        {
            // Create temp 
            node *tmp = cursor;

            // Move cursor to next node
            cursor = cursor->next;

            // Free up temp
            free(tmp);
        }
        // If cursor is NULL
        if (i == N - 1 && cursor == NULL)
        {
            return true;
        }
    }
    return false;
}
