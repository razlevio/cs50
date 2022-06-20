# [Guessing Game](https://cs50.harvard.edu/python/2022/psets/4/game/#guessing-game)

I’m thinking of a number between 1 and 100…

What is it?

It’s 50! But what if it were more random?

In a file called `game.py`, implement a program that:

- Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and n, inclusive.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
  - If the guess is smaller than that integer, the program should output `Too small!` and prompt the user again.
  - If the guess is larger than that integer, the program should output `Too large!` and prompt the user again.
  - If the guess is the same as that integer, the program should output `Just right!` and exit.
