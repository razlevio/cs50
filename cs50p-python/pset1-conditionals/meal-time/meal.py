def main():
    inp = input("What time is it? ").strip()
    t = convert(inp)
    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")


def convert(time):
    # breakfast 07:00 to 08:00
    # lunch     12:00 to 13:00
    # dinner    18:00 to 19:00
    break_time = time.split(":")
    hour = break_time[0]
    minutes = round((float(break_time[1]) / 60), 2)
    if len(hour) == 1:
        return int(hour)+minutes
    elif len(hour) > 1 and hour[0] == 0:
        hour = hour[1:]
        return int(hour)+minutes
    else:
        return int(hour)+minutes


if __name__ == '__main__':
    main()
