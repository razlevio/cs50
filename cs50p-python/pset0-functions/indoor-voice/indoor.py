def main():
    inp = input("Insert string: ")
    res = ""
    for ch in inp:
        if ch.isalpha():
            res += ch.lower()
        else:
            res += ch
    print(res)


if __name__ == "__main__":
    main()
