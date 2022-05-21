def main():
    print(prompt_user())


def prompt_user():
    while True:
        inp = input("Fraction: ")
        inp = inp.split("/")
        try:
            first_num = int(inp[0])
        except ValueError:
            continue
        try:
            second_num = int(inp[1])
            if second_num == 0:
                continue
        except ValueError:
            continue
        try:
            if first_num > second_num:
                continue
            else:
                div = first_num / second_num
        except ZeroDivisionError:
            continue
        else:
            percentage = div*100
            if percentage > 99:
                return "F"
            elif percentage < 1:
                return "E"
            else:
                return f"{int(percentage)}%"


if __name__ == '__main__':
    main()
