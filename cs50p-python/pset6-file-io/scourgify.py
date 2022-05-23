from sys import exit, argv
import csv


def main():
    process_cli_arguments()
    process_csv(argv[1], argv[2])


def process_cli_arguments():
    arguments = len(argv)
    if arguments == 3 and ((not argv[1].endswith(".csv")) or (not argv[2].endswith(".csv"))):
        exit("One or both of files provided are not CSV files")
    if arguments < 3:
        exit("Too few command-line arguments")
    if arguments > 3:
        exit("Too many command-line arguments")


def process_csv(input_csv_name, output_csv_name):
    try:
        with open(input_csv_name, "r") as before:
            reader = csv.reader(before, quotechar=(","))
            next(reader)
            with open(output_csv_name, "w") as after:
                writer = csv.writer(after)
                writer.writerow(["first", "last", "house"])
                for row in reader:
                    row = [line.replace('"', "") for line in row]
                    row = [line.replace(" ", "") for line in row]
                    last_name = row[0]
                    first_name = row[1]
                    house = row[2]
                    row = [f"{first_name}", f"{last_name}", house]
                    writer.writerow(row)
    except FileNotFoundError:
        exit(f"Could not read {input_csv_name}")


if __name__ == "__main__":
    main()
