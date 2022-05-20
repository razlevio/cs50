# [Math Interpreter](https://cs50.harvard.edu/python/2022/psets/1/interpreter/#math-interpreter)

Python already supports math, whereby _you_ can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables _users_ to do math, even without knowing Python.

In a file called `interpreter.py`, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as `x y z`, with one space between `x` and `y` and one space between `y` and `z`, wherein:

- `x` is an integer
- `y` is `+`, `-`, `*`, or `/`
- `z` is an integer

For instance, if the user inputs `1 + 1`, your program should output `2.0`. Assume that, if `y` is `/`, then `z` will not be `0`.

Note that, just as `python` itself is an interpreter for Python, so will your `interpreter.py` be an interpreter for math!
