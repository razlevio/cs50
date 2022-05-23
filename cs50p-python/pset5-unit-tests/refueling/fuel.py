from sys import exit


def main():
    print(gauge(convert("three/four")))


def convert(fraction):
    num = fraction.split("/")
    numerator = int(num[0])
    denominator = int(num[1])
    percent = numerator / denominator * 100
    if 0 <= percent <= 100:
        return int(percent)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
