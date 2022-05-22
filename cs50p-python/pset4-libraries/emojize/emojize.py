import emoji


def main():
    inp = input("Input: ").strip().lower()
    inp_converted = emoji.emojize(inp, language='alias')
    is_emoji = emoji.is_emoji(inp_converted)
    if is_emoji:
        print(f"Output: {inp_converted}")


if __name__ == "__main__":
    main()
