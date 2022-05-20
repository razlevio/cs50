def main():
    inp = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if inp.strip() == "42" or inp.lower().strip() == "forty-two" or inp.lower().strip() == "forty two":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
