def main():
    # Coke costs = 50 cents
    # Accepted coins:
    #   25 cents
    #   10 cents
    #   5 cents
    coke_price = 50
    coin_inserted = None
    while True:
        coin_inserted = coin_validation(coke_price)
        if coin_inserted == 50:
            continue
        coke_price -= coin_inserted
        if coke_price < 0 or coke_price == 0:
            print(f"Change Owed: {abs(coke_price)}")
            break


def coin_validation(coke_price):
    while True:
        print(f"Amount Due: {coke_price}")
        coin = int(input("Insert Coin: ").strip())
        if coin == 5 or coin == 10 or coin == 25:
            break
    return coin


if __name__ == "__main__":
    main()
