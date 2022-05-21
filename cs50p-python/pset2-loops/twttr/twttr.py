import re


def main():
    inp = input("Input: ").strip()
    res = ""
    pattern = "aeiouAEIOU"
    for ch in inp:
        if ch not in pattern:
            res += ch
    print(res)

    # Additional sophisticated approach:
    # print(re.sub("[aeiouAEIOU]", "", inp))


if __name__ == '__main__':
    main()
