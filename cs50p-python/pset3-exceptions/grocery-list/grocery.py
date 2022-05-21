def main():
    items = dict()
    while True:
        try:
            item = input().strip().lower()
        except EOFError:
            break
        else:
            if item not in items.keys():
                items[item] = 1
            else:
                items[item] += 1
    print_items(items)


def print_items(items):
    sorted_keys = sorted(items)
    for item in sorted_keys:
        print(f"{items[item]} {item.upper()}")


if __name__ == '__main__':
    main()
