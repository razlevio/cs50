def main():
    inp = input("Greeting: ").lower()
    if "hello" in inp:
        print("$0")
    elif inp[0] == "h":
        print("$20")
    else:
        print("$100")


if __name__ == '__main__':
    main()
