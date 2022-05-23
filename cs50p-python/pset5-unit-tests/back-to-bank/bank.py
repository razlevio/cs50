from sys import exit


def main():
    inp = input("Greeting: ").strip()
    print(value(inp))
    exit()


def value(greeting):
    if greeting == "" or greeting.isnumeric():
        exit("invalid input\n")
    greeting = greeting.lower()
    words = greeting.split(" ")
    if words[0] == "hello":
        return 0
    elif words[0][0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
