from sys import exit, argv


def main():
    process_cli_arguments()
    file_name = argv[1]
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        exit("File does not exist")
    else:
        print(process_file(file))
        file.close()


def process_cli_arguments():
    if len(argv) == 2 and not argv[1].endswith(".py"):
        exit("Not a Python file")
    if len(argv) < 2:
        exit("Too few command-line arguments")
    if len(argv) > 2:
        exit("Too many command-line arguments")


def process_file(file):
    counter = 0
    for line in file:
        if line.isspace():
            continue
        for ch in line:
            if ch == " ":
                continue
            elif ch == "#":
                break
            else:
                counter += 1
                break
    return counter


if __name__ == "__main__":
    main()
