# [camelCase](https://cs50.harvard.edu/python/2022/psets/2/camel/#camelcase)

![camel](https://cs50.harvard.edu/python/2022/psets/2/camel/1024px-CamelCase_new.svg.png)

Source: [en.wikipedia.org/wiki/Camel_case](https://en.wikipedia.org/wiki/Camel_case)

In some languages, it’s common to use [camel case](https://en.wikipedia.org/wiki/Camel_case) (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called `name`, a variable for a user’s first name might be called `firstName`, and a variable for a user’s preferred first name (e.g., nickname) might be called `preferredFirstName`.

Python, by contrast, [recommends](https://peps.python.org/pep-0008/#function-and-variable-names) [snake case](https://en.wikipedia.org/wiki/Snake_case), whereby words are instead separated by underscores (`_`), with all letters in lowercase. For instance, those same variables would be called `name`, `first_name`, and `preferred_first_name`, respectively, in Python.

In a file called `camel.py`, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
