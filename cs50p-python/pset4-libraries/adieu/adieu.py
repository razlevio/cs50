def main():
    names = []
    while True:
        try:
            inp = input("Name: ").strip().title()
        except EOFError:
            print()
            break
        else:
            names.append(inp)

    prefix = "Adieu, adieu, to "
    number_of_names = len(names)
    if number_of_names == 1:
        print(f"{prefix}{names[0]}")
    elif number_of_names == 2:
        print(f"{prefix}{names[0]} and {names[1]}")
    else:
        for name in names[:(len(names)-1)]:
            prefix += f"{name}, "
        prefix += f"and {names[-1]}"
        print(prefix)


if __name__ == '__main__':
    main()
