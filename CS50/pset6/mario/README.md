# [Mario Regular](https://cs50.harvard.edu/x/2021/psets/6/mario/less/#mario)

![screenshot of Mario jumping up pyramid](https://cs50.harvard.edu/x/2021/psets/6/mario/less/pyramid.png)

Implement a program that prints out a half-pyramid of a specified height, per the below.

```
$ python mario.py
Height: 4
   #
  ##
 ###
####
```

## Specification

-   Write, in a file called  `mario.py`  in  `~/pset6/mario/less/`, a program that recreates the half-pyramid using hashes (`#`) for blocks, exactly as you did in  [Problem Set 1](https://cs50.harvard.edu/x/2021/psets/1/), except that your program this time should be written in Python.
-   To make things more interesting, first prompt the user with  `get_int`  for the half-pyramid’s height, a positive integer between  `1`  and  `8`, inclusive.
-   If the user fails to provide a positive integer no greater than  `8`, you should re-prompt for the same again.
-   Then, generate (with the help of  `print`  and one or more loops) the desired half-pyramid.
-   Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.

## Usage
Your program should behave per the example below.

```
$ python mario.py
Height: 4
   #
  ##
 ###
####
```


# [Mario Advanced](https://cs50.harvard.edu/x/2021/psets/6/mario/more/#mario)

![screenshot of Mario jumping up pyramid](https://cs50.harvard.edu/x/2021/psets/6/mario/more/pyramids.png)

Implement a program that prints out a double half-pyramid of a specified height, per the below.

```
$ python mario.py
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####

```

## Specification
-   Write, in a file called  `mario.py`  in  `~/pset6/mario/more/`, a program that recreates these half-pyramids using hashes (`#`) for blocks, exactly as you did in  [Problem Set 1](https://cs50.harvard.edu/x/2021/psets/1/), except that your program this time should be written in Python.
-   To make things more interesting, first prompt the user with  `get_int`  for the half-pyramid’s height, a positive integer between  `1`  and  `8`, inclusive. (The height of the half-pyramids pictured above happens to be  `4`, the width of each half-pyramid  `4`, with a gap of size  `2`  separating them).
-   If the user fails to provide a positive integer no greater than  `8`, you should re-prompt for the same again.
-   Then, generate (with the help of  `print`  and one or more loops) the desired half-pyramids.
-   Take care to align the bottom-left corner of your pyramid with the left-hand edge of your terminal window, and ensure that there are two spaces between the two pyramids, and that there are no additional spaces after the last set of hashes on each row.

## Usage

Your program should behave per the example below.

```
$ python mario.py
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
```
