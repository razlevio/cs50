# MM/DD/YYYY -> middle-endian date order
# YYYY-MM-DD -> ISO-8601 (what computers use)

# valid inputs:
#   MM/DD/YYYY
#   Month M (or MM), YYYY

def main():
    while True:
        date = input("Date: ").strip()
        validation = inp_processing(date)
        if validation == False:
            continue
        elif isinstance(validation, str):
            print(validation)
            break


""" Handling the user input by checking the input length constraint of
    and checking the type of date endian or verbose. After ensuring input is validated
    convert the date using the respective conversion function """


def inp_processing(inp):
    # general errors with the input
    if inp == "":
        return False
    if len(inp) < 8:
        return False

    input_type = type_of_date(inp)
    if input_type == "endian":
        return convert_endian(inp)
    elif input_type == "verbose":
        return convert_verbose(inp)
    else:
        return False


""" Checking if the date inserted is endian or verbose """


def type_of_date(inp):
    endian = not any(ch.isalpha() for ch in inp)
    verbose = any(ch.isalpha() for ch in inp)
    if endian:
        return "endian"
    elif verbose:
        return "verbose"
    else:
        return False


""" Converting endian date to the computer date """


def convert_endian(inp):
    # return endian representation or if not valid False
    if len(inp) > 10:
        return False
    try:
        month, day, year = inp.split("/")
    except ValueError:
        return False
    else:
        try:
            month = int(month)
            day = int(day)
        except ValueError:
            return False
        else:
            if month < 1 or month > 12:
                return False
            elif day < 1 or day > 31:
                return False
            elif len(year) != 4:
                return False
            else:
                return f"{year}-{month:02}-{day:02}"


""" Converting verbose date to computer date """


def convert_verbose(inp):
    # return verbose representation or if not valid False
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    try:
        inp.index(",")
    except ValueError:
        return False
    else:
        inp = inp.replace(",", "")

    try:
        month, day, year = inp.split(" ")
    except ValueError:
        return False
    else:
        if month.title() not in months:
            return False
        if len(year) != 4:
            return False

        try:
            day = int(day)
        except ValueError:
            return False
        else:
            if day < 1 or day > 31:
                return False
            else:
                return f"{year}-{(months.index(month)+1):02}-{day:02}"


if __name__ == '__main__':
    main()
