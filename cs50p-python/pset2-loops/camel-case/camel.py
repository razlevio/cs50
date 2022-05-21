def main():
    inp = input("camelCase: ").strip()
    res = ""
    for ch in inp:
        if ch.isupper():
            res += "_"
            res += ch.lower()
        else:
            res += ch
    print(res)


if __name__ == "__main__":
    main()
