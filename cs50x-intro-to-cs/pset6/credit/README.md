
# [Credit](https://cs50.harvard.edu/x/2021/psets/6/credit/#credit)

Implement a program that determines whether a provided credit card number is valid according to Luhn’s algorithm.

```
$ python credit.py
Number: 378282246310005
AMEX

```

## Specification

-   In  `credit.py`  in  `~/pset6/credit/`, write a program that prompts the user for a credit card number and then reports (via  `print`) whether it is a valid American Express, MasterCard, or Visa card number, exactly as you did in  [Problem Set 1](https://cs50.harvard.edu/x/2021/psets/1/), except that your program this time should be written in Python.
-   So that we can automate some tests of your code, we ask that your program’s last line of output be  `AMEX\n`  or  `MASTERCARD\n`  or  `VISA\n`  or  `INVALID\n`, nothing more, nothing less.
-   For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
-   Best to use  `get_int`  or  `get_string`  from CS50’s library to get users’ input, depending on how you to decide to implement this one.

## Usage
Your program should behave per the example below.

```
$ python credit.py
Number: 378282246310005
AMEX
```
