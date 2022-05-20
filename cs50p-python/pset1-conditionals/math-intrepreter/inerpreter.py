def main():
    expr = input("Expression: ")
    arr = expr.split(" ")
    x = float(arr[0])
    operator = arr[1]
    y = float(arr[2])

    if operator == "+":
        print(round((x+y), 1))
    elif operator == "-":
        print(round((x-y), 1))
    elif operator == "/":
        print(round((x/y), 1))
    elif operator == "*":
        print(round((x*y), 1))


if __name__ == "__main__":
    main()
