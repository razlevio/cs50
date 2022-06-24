import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """ Convert function to conver from AM/PM hours to 24 Hours """

    # AM conversion dictionary
    am_conversion = {
        "12": "00",
        "1": "01",
        "2": "02",
        "3": "03",
        "4": "04",
        "5": "05",
        "6": "06",
        "7": "07",
        "8": "08",
        "9": "09",
        "10": "10",
        "11": "11",
    }

    # PM converion dictionary
    pm_conversion = {
        "12": "12",
        "1": "13",
        "2": "14",
        "3": "15",
        "4": "16",
        "5": "17",
        "6": "18",
        "7": "19",
        "8": "20",
        "9": "21",
        "10": "22",
        "11": "23",
    }

    str_proccesing = ""
    res = []
    s = s.upper()
    splitted_hours = s.split("TO")
    for hour in splitted_hours:
        hour = hour.strip()
        pattern = re.search(r"(^(0?[1-9]|1[0-2]):([0-5]\d)\s?((?:A|P)M)$)|(^(0?\d|1[0-2])\s?((?:A|P)M)$)", hour)
        if pattern:
            time, abbv = hour.split(" ")
            time = time.split(":")
            if len(time) == 1:
                hours = time[0]
                if abbv == "AM":
                    str_proccesing = f"{am_conversion[hours]}:00"
                elif abbv == "PM":
                    str_proccesing = f"{pm_conversion[hours]}:00"
            else:
                hours = time[0]
                minutes = time[1]
                if abbv == "AM":
                    str_proccesing = f"{am_conversion[hours]}:{minutes}"
                elif abbv == "PM":
                    str_proccesing = f"{pm_conversion[hours]}:{minutes}"
        else:
            raise ValueError("Wrong time pattern")
        res.append(str_proccesing)
    return " to ".join(res)


if __name__ == "__main__":
    main()
