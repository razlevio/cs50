# [File Extensions](https://cs50.harvard.edu/python/2022/psets/1/extensions/#file-extensions)

Even though Windows and macOS sometimes hide them, most files have [file extensions](https://en.wikipedia.org/wiki/Filename_extension), a suffix that starts with a period (`.`) at the end of their name. For instance, file names for [GIFs](https://en.wikipedia.org/wiki/GIF) end with `.gif`, and file names for [JPEGs](https://en.wikipedia.org/wiki/JPEG) end with `.jpg` or `.jpeg`. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on [media types](https://en.wikipedia.org/wiki/Media_type), formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an [HTTP header](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields), along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is `image/gif`, and the media type for a JPEG is `image/jpeg`. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

See [developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) for common types.

In a file called `extensions.py`, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

- `.gif`
- `.jpg`
- `.jpeg`
- `.png`
- `.pdf`
- `.txt`
- `.zip`

If the file’s name ends with some other suffix or has no suffix at all, output `application/octet-stream` instead, which is a common default.
