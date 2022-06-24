import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    word = "um"
    matches = len(re.findall(r'\b'+ word + r'\b', s, re.IGNORECASE))
    return matches


if __name__ == "__main__":
    main()
