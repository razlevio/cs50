# [CS50 P-Shirt](https://cs50.harvard.edu/python/2022/psets/6/shirt/#cs50-p-shirt)

![CS50 shirt](https://cs50.harvard.edu/python/2022/psets/6/shirt/took.png)

After finishing CS50 itself, students on campus at Harvard traditionally receive their very own [I took CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt) t-shirt. No need to buy one online, but like to try one on virtually?

In a file called `shirt.py`, implement a program that expects exactly two command-line arguments:

- in `sys.argv[1]`, the name (or path) of a JPEG or PNG to read (i.e., open) as input
- in `sys.argv[2]`, the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay [shirt.png](https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png) (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with `Image.open`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open), resize and crop the input with `ImageOps.fit`, per [pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit](https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit), using default values for `method`, `bleed`, and `centering`, overlay the shirt with `Image.paste`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste), and save the result with `Image.save`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save).

The program should instead exit via `sys.exit`:

- if the user does not specify exactly two command-line arguments,
- if the input’s and output’s names do not end in `.jpg`, `.jpeg`, or `.png`, case-insensitively,
- if the input’s name does not have the same extension as the output’s name, or
- if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like [these demos](https://cs50.harvard.edu/python/2022/psets/6/shirt/#demos), so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as `shirt.py`. No need to submit any photos with your code. But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of [CS50’s communities](https://cs50.harvard.edu/python/communities)!

### Before

[![before](https://cs50.harvard.edu/python/2022/psets/6/shirt/before1.jpg)](https://cs50.harvard.edu/python/2022/psets/6/shirt/before1.jpg) [![before](https://cs50.harvard.edu/python/2022/psets/6/shirt/before2.jpg)](https://cs50.harvard.edu/python/2022/psets/6/shirt/before2.jpg) [![before](https://cs50.harvard.edu/python/2022/psets/6/shirt/before3.jpg)](https://cs50.harvard.edu/python/2022/psets/6/shirt/before3.jpg)

### After

![after](https://cs50.harvard.edu/python/2022/psets/6/shirt/after1.jpg) ![after](https://cs50.harvard.edu/python/2022/psets/6/shirt/after2.jpg) ![after](https://cs50.harvard.edu/python/2022/psets/6/shirt/after3.jpg)
