def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


""" Function that returns if the user input is valid by calling helper functions
    this function is for handling all of the restrictions of plates numbers """


def is_valid(s):
    if valid_len(s) and start_with_two_letters(s) and symbols_valdiation(s) and first_num_not_zero(s) and numbers_in_middle(s):
        return True
    else:
        return False


""" Validate that the plate is in valid length between 2 to 6 character """


def valid_len(s):
    if len(s) > 6 or len(s) < 2:
        return False
    else:
        return True


""" Validate if the plate starts with two letters as needed by restrictions """


def start_with_two_letters(s):
    if len(s) < 2:
        return False
    elif s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False


""" Validate that the plate doesn't have any of the not allowed symbols """


def symbols_valdiation(s):
    pattern = " .,!@#$%^&`*/-+)(}{'\""
    for ch in s:
        if ch in pattern:
            return False
    return True


""" Validate that the first number in the plate is not zero """


def first_num_not_zero(s):
    first_letter_checked = False
    if s.isalpha():
        return True
    else:
        for ch in s:
            if first_letter_checked == False and ch.isnumeric():
                first_letter_checked == True
                if ch == "0":
                    return False
                else:
                    return True
            elif first_letter_checked:
                break


""" Validate that the palte numbers not used in the middle of a plate; they must come at the end. """


def numbers_in_middle(s):
    s = s[2:]
    length = len(s)
    if length == 1:
        return True
    elif length == 2:
        return two_digits_validation(s)
    elif length == 3:
        three_digits_validation(s)
    elif length == 4:
        if s[0].isalpha() and three_digits_validation(s[1:]):
            return True
        elif s[0].isnumeric() and not three_digits(s[1:]):
            return False
        else:
            return True


""" Helper function to the numbers_in_middle function """


def two_digits_validation(s):
    if s.isalpha() or s.isnumeric():
        return True
    elif s[0].isalpha():
        return True
    else:
        return False


""" Helper function to the numbers_in_middle function """


def three_digits_validation(s):
    if s.isalpha() or s.isnumeric():
        return True
    elif s[0].isnumeric() and s[2].isalpha():
        return False
    elif s[0].isalpha():
        s = s[1:]
        return two_digits_validation(s)
    else:
        return False


if __name__ == '__main__':
    main()
