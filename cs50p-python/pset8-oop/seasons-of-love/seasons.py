from datetime import date
from sys import exit
import re
import inflect


def main():
    """
    Prompting the user to insert his birthday, outputting the number of minutes
    in words that have been passed since he was born
    """
    birthday = date_validation(input("Date of Birth: ").strip())
    minutes = minutes_since_birthday(birthday)
    print(generate_words(minutes))


def date_validation(date):
    """
    Validate that a certain date is valid date

    :param date: The date to check
    :type date: str
    :raise SystemExit: If date is not a valid date in the form YYYY-MM-DD
    :return: The date only if its valid
    :rtype: str
    """
    if not re.fullmatch(r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$", date):
        exit("Invalid date")
    else:
        return date


def minutes_since_birthday(birthday):
    """
    Calucation the number of minutes passed since a birthday date

    :param birthday: The acutal birthday date
    :type birthday: str
    :return: The number of minutes
    :rtype: int
    """
    today = date.today()
    delta = today-date.fromisoformat(birthday)
    days = delta.days
    minutes = round(days * 1440) # 1440 minutes in a day
    return minutes


def generate_words(minutes):
    """
    Generate words from number, 1234 = thousand, two hundred, thirthy four

    :param minutes: Number of minutes
    :type minutes: int
    :return: The words represeting the number provided
    :rtype: str
    """
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"


if __name__ == "__main__":
    main()
