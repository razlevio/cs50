
# [Cookie Jar](https://cs50.harvard.edu/python/2022/psets/8/jar/#cookie-jar)

![Cookie Monster](https://cs50.harvard.edu/python/2022/psets/8/jar/giphy1.gif)

Source: Sesame Street

Suppose that you’d like to implement a  [cookie jar](https://en.wikipedia.org/wiki/Cookie_jar)  in which to store cookies. In a file called  `jar.py`, implement a  `class`  called  `Jar`  with these methods:

-   `__init__`  should initialize a cookie jar with the given  `capacity`, which represents the maximum number of cookies that can fit in the cookie jar. If  `capacity`  is not a non-negative  `int`, though,  `__init__`  should instead raise a  `ValueError`.
-   `__str__`  should return a  `str`  with  n  `🍪`, where  n  is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then  `str`  should return  `"🍪🍪🍪"`
-   `deposit`  should add  `n`  cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though,  `deposit`  should instead raise a  `ValueError`.
-   `withdraw`  should remove  `n`  cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though,  `withdraw`  should instead raise a  `ValueError`.
-   `capacity`  should return the cookie jar’s capacity.
-   `size`  should return the number of cookies actually in the cookie jar.

additionally implement, in a file called  `test_jar.py`,  **four or more**  functions that collectively test your implementation of  `Jar`  thoroughly, each of whose names should begin with  `test_`  so that you can execute your tests with:

```
pytest test_jar.py
```
