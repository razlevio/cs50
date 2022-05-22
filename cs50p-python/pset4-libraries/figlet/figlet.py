from sys import argv, exit
from pyfiglet import Figlet
import random


def main():
    """ information about the command line arguments and initialization of figlet object """
    arguments_num = len(argv)
    fidglet = Figlet()
    fonts = fidglet.getFonts()

    if arguments_num == 1:
        """ if there are none command line arguments choose random font
            then prompt user for input and print the input in the random fidglet font """
        print_random_fidglet(fidglet, fonts)

    elif arguments_num == 3:
        """ if there are three command line arguments, validate that the arguments are valid
            and if they do prompt the user for input, set the requested font and print the input
            in the choosen fidglet font """
        flag = argv[1]
        font_name = argv[2]
        valid = arguments_validation(flag, font_name, fonts)
        if valid:
            print_fidglet(fidglet, fonts, font_name)
        else:
            exit("Invalid usage")
    else:
        exit("Invalid usage")


def arguments_validation(flag, font_name, fonts):
    """ function to validate that the command arguments are valid
        command arguments can be -f or --font for the first argument
        and for second argument to be valid it needs to be a font that included in the fonts array """
    if flag != "-f" and flag != "--font":
        return False
    else:
        if font_name in fonts:
            return True
        else:
            return False


def print_random_fidglet(fidglet, fonts):
    """ choosing a random font from the fonts array, setting this font to the fidglet object
        prompt the user for text input and then print the input as rendered fidglet of the requested font """
    fidglet.setFont(font=random.choice(fonts))
    inp = input("Input: ").strip()
    print(fidglet.renderText(inp))


def print_fidglet(fidglet, fonts, font_name):
    """ setting the fidglet object font to the provided user requested font
        prompt the user for text input and then print the input as rendered fidglet of the requested font """
    fidglet.setFont(font=font_name)
    inp = input("Input: ").strip()
    print(fidglet.renderText(inp))


if __name__ == '__main__':
    main()
