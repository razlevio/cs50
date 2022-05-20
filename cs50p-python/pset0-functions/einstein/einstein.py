def main():
    # Prompt user for mass in kg as integer
    mass = int(input("m: "))

    # E = mc^2
    # E = energy in joules
    # c = speed of light 300000000 meter per second
    # Output the energy value
    energy = mass*300000000**2
    print(f"e: {energy}")


if __name__ == '__main__':
    main()
