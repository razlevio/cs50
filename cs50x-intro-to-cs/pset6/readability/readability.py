from cs50 import get_string

def main():
    text = get_string("Text: ")
    numWords = 0
    numSent = 0
    numLet = 0
    i = 0
    length = len(text)

    while i < length:
        if text[i].isalpha():
            numLet += 1
        if (i == 0 and text[i] != " ") or (i != length and text[i] == " " and text[i + 1] != " "):
            numWords += 1
        if text[i] == "." or text[i] == "?" or text[i] == "!":
            numSent += 1
        i += 1
    calcL = (numLet / numWords) * 100
    calcS = (numSent / numWords) * 100
    index = round(0.0588 * calcL - 0.296 * calcS - 15.8)
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

if __name__ == "__main__":
    main()

