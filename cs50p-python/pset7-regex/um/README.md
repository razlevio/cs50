# [Regular, um, Expressions](https://cs50.harvard.edu/python/2022/psets/7/um/#regular-um-expressions)

It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The more you do it, though, the more noticeable it tends to be!

In a file called  `um.py`, implement a function called  `count`  that expects a line of text as input as a  `str`  and returns, as an  `int`, the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. For instance, given text like  `hello, um, world`, the function should return  `1`. Given text like  `yummy`, though, the function should return  `0`.

Either before or after you implement  `count`  in  `um.py`, additionally implement, in a file called  `test_um.py`,  **three or more**  functions that collectively test your implementation of  `count`  thoroughly, each of whose names should begin with  `test_`  so that you can execute your tests with:

```
pytest test_um.py
```
