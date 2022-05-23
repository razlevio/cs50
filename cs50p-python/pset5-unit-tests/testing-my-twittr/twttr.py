def main():
    inp = input("Input: ")
    print(shorten(inp))


def shorten(word):
    vowels = "aeiouAEIOU"
    res = ""
    for ch in word:
        if ch not in vowels:
            res += ch
    return res


if __name__ == "__main__":
    main()
