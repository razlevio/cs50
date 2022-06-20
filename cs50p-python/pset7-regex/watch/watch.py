import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    youtube_url = re.search(r"\"https?://(www\.)?youtube\.com/embed/(\w+)\"", s, re.IGNORECASE)
    if youtube_url:
        url_code = youtube_url.group(2)
        return f"https://youtu.be/{url_code}"


if __name__ == "__main__":
    main()
