def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
    # Remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
    d = d.replace("$", "")
    return(float(d))


def percent_to_float(p):
    # Accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage
    # as a float. For instance, given 15% as input, it should return 0.15.
    p = p.replace("%", "")
    if float(p) > 99:
        mult = p[0:(len(p)-2)]
        rest = p[len(p)-2:]
        p = f"{mult}.{rest}"
    elif float(p) < 10:
        p = f"0.0{p}"
    else:
        p = f"0.{p}"
    return float(p)


main()
