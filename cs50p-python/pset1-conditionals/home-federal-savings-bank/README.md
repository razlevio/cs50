# [Home Federal Savings Bank](https://cs50.harvard.edu/python/2022/psets/1/bank/#home-federal-savings-bank)

In [season 7, episode 24](https://en.wikipedia.org/wiki/The_Invitations) of [Seinfeld](https://en.wikipedia.org/wiki/Seinfeld), [Kramer](https://en.wikipedia.org/wiki/Cosmo_Kramer) visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output `$0`. If the greeting starts with an “h” (but not “hello”), output `$20`. Otherwise, output `$100`. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
