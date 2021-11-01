from sys import argv, exit
import csv


def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    shortTandemRepeats = []
    profiles = []

    with open(argv[1], mode="r") as database:
        reader = csv.DictReader(database)
        # Populate list of shortTandemRepeats
        shortTandemRepeats = reader.fieldnames[1:]
        for row in reader:
            # Add a person to profiles
            profiles.append(row)

    # Initialize dictionary for sequence file
    strCount = dict.fromkeys(shortTandemRepeats, 0)

    # Read the sequence file
    with open(argv[2], mode="r") as sequenceFile:
        sequence = sequenceFile.readline()
        for shortTandemRepeat in shortTandemRepeats:
            strCount[shortTandemRepeat] = find_repeats(sequence, shortTandemRepeat)

    # Check if any person has same the amount of shortTandemRepeat as sequence
    for profile in profiles:
        matchCount = 0

        for shortTandemRepeat in shortTandemRepeats:
            if int(profile[shortTandemRepeat]) != strCount[shortTandemRepeat]:
                continue
            matchCount += 1

        if matchCount == len(shortTandemRepeats):
            print(profile['name'])
            exit(0)

    print("No match")
    exit(1)


def find_repeats(sequence, shortTandemRepeat):
    k = len(shortTandemRepeat)

    maxRepeats = 0
    for i in range(len(sequence)):
        # Initialize and reset the repeat counter
        repeats = 0
        if sequence[i: i + k] == shortTandemRepeat:
            repeats += 1
            while sequence[i: i + k] == sequence[i + k: i + (2 * k)]:
                repeats += 1
                i += k

        # Update the max count
        if repeats > maxRepeats:
            maxRepeats = repeats

    return maxRepeats


if __name__ == "__main__":
    main()