from random import randint
from sys import exit


def main():
    level = user_input_handler("Level")
    rand = randint(1, level)
    while True:
        guess = user_input_handler("Guess")
        if guess < rand:
            print("Too small!")
            continue
        elif guess > rand:
            print("Too large!")
            continue
        else:
            print("Just right!")
            exit("Thanks for playing")


def user_input_handler(type):
    while True:
        try:
            inp = int(input(f"{type}: "))
        except ValueError:
            continue
        else:
            if inp < 1:
                continue
            else:
                return inp


if __name__ == "__main__":
    main()
