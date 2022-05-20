def main():
    file_name = input("File name: ").strip().lower()
    dot_count = file_name.count(".")
    if dot_count == 0:
        print("application/octet-stream")
    elif dot_count == 1:
        extension = file_name[file_name.index(".")+1:]
        print(extension_match(extension))
    else:
        while dot_count > 1:
            file_name = file_name.replace(".", "", 1)
            dot_count -= 1
        extension = file_name[file_name.index(".")+1:]
        print(extension_match(extension))


def extension_match(extension):
    if extension == "gif" or extension == "jpg" or extension == "jpeg" or extension == "png":
        if extension == "jpg":
            return "image/jpeg"
        else:
            return f"image/{extension}"
    elif extension == "pdf" or extension == "zip":
        return f"application/{extension}"
    elif extension == "txt":
        return "text/plain"
    else:
        return "application/octet-stream"


if __name__ == "__main__":
    main()
