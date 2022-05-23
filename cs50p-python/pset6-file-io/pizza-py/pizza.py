from sys import exit, argv
from tabulate import tabulate
import csv


def main():
    process_cli_arguments()
    process_csv(argv[1])


def process_cli_arguments():
    argumnets = len(argv)
    if argumnets == 2 and not argv[1].lower().endswith(".csv"):
        exit("Not a CSV file")
    if argumnets < 2:
        exit("Too few command-line arguments")
    if argumnets > 2:
        exit("Too many command-line arguments")


def process_csv(csv_file):
    res = []
    try:
        with open(csv_file, "r") as data:
            reader = csv.reader(data)
            for row in reader:
                res.append(row)
            print(tabulate(res[1:], headers=res[0], tablefmt="grid"))
    except FileNotFoundError:
        exit("File does not exist")


if __name__ == "__main__":
    main()
