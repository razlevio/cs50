
# [CS50 Shirtificate](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/#cs50-shirtificate)

[![John Harvard's CS50 Shirtificate](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.png)](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.pdf)

Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an  [I took CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt)  t-shirt,  [shirtificate.png](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png), customized with a user’s own name.

In a file called  `shirtificate.py`, implement a program that prompts the user for their name and outputs, using  [fpdf2](https://pypi.org/project/fpdf2/), a CS50 shirtificate in a file called  `shirtificate.pdf`  similar to  [this one for John Harvard](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.pdf), with these specifications:

-   The  [orientation](https://pyfpdf.github.io/fpdf2/PageFormatAndOrientation.html)  of the PDF should be Portrait.
-   The  [format](https://pyfpdf.github.io/fpdf2/PageFormatAndOrientation.html)  of the PDF should be A4, which is 210mm wide by 297mm tall.
-   The top of the PDF should “CS50 Shirtificate” as  [text](https://pyfpdf.github.io/fpdf2/Text.html), centered horizontally.
-   The shirt’s  [image](https://pyfpdf.github.io/fpdf2/Images.html)  should be centered horizontally.
-   The user’s name should be on top of the shirt, in white  [text](https://pyfpdf.github.io/fpdf2/TextStyling.html).

All other details we leave to you. You’re even welcome to add borders, colors, and  [lines](https://pyfpdf.github.io/fpdf2/Shapes.html#lines). Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s  [tutorial](https://pyfpdf.github.io/fpdf2/Tutorial.html)  to learn how to use it. Then skim fpdf2’s  [API](https://pyfpdf.github.io/fpdf2/fpdf/)  (application programming interface) to see all of its functions and parameters therefor.
