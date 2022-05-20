def main():
    inp = input().strip()
    print(convert(inp))


def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string


if __name__ == "__main__":
    main()
