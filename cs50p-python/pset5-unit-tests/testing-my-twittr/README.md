# [Testing my twttr](https://cs50.harvard.edu/python/2022/psets/5/test_twttr/#testing-my-twttr)

In a file called `twttr.py`, reimplement [Setting up my twttr](https://cs50.harvard.edu/python/2022/psets/2/twttr/) from [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/), restructuring your code per the below, wherein `shorten` expects a `str` as input and returns that same `str` but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

```
def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()

```

Then, in a file called `test_twttr.py`, implement **one or more** functions that collectively test your implementation of `shorten` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_twttr.py
```
