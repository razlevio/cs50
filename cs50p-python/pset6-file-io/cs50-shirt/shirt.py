from sys import argv, exit
from PIL import Image, ImageOps
import os

""" program to take a shirt predefined img, and paste it on an img
    the img is provided as a path to that img from cli argument
    the program will reject any file that is not existed or that dosent have .jpg, .jpeg or .png extension
    the program will take exactly two cli arguments the name of the base img to paste the shirt on it
    and the name for the saved file with the base photo and the shirt paste on it """


def main():
    process_cli_arguments()
    shirt_file_name = "shirt.png"
    input_file_name = argv[1]
    output_file_name = argv[2]
    # open the base photo and the shirt photo
    shirt_img = open_input_file(shirt_file_name)
    input_img = open_input_file(input_file_name)
    # cropping the base img so it will fit the shirt img size
    input_img = ImageOps.fit(input_img, size=shirt_img.size,
                             method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    # pasting the shirt img over the base img and save the results to an output file
    input_img.paste(shirt_img, mask=shirt_img)
    input_img.save(output_file_name)
    # closing the img files
    input_img.close()
    shirt_img.close()


""" function to process the provided command-line arguments
    program must include two cli arguments and those argumentes
    must have .jpg/.jpeg/.png extenions """


def process_cli_arguments():
    arguments = len(argv)
    allowed_extensions = [".jpg", ".jpeg", ".png"]
    if arguments == 3:
        input_file_name = argv[1].lower()
        input_extension = os.path.splitext(input_file_name)[1]
        output_file_name = argv[2].lower()
        output_extension = os.path.splitext(output_file_name)[1]
        # Wrong input extension but both are same
        if input_extension == "" or output_extension == "":
            exit("Input or output or both file extension are missed")
        if input_extension != output_extension:
            exit("Input and output have different extensions")
        else:
            if input_extension not in allowed_extensions:
                exit("Extensions are not allowed")

    if arguments < 3:
        exit("Too few command-line arguments")
    if arguments > 3:
        exit("Too many command-line arguments")


""" function to open the base img file, if the file is not exists
    exit with an error, otherwise return the opened img object """


def open_input_file(input_file_name):
    try:
        return Image.open(input_file_name, "r")
    except FileNotFoundError:
        exit("Input file does not exists")


if __name__ == "__main__":
    main()
