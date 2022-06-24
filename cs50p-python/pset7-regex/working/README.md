# [Working 9 to 5](https://cs50.harvard.edu/python/2022/psets/7/working/#working-9-to-5)

Whereas  [most countries](https://en.wikipedia.org/wiki/Date_and_time_representation_by_country#Time)  use a  [24-hour clock](https://en.wikipedia.org/wiki/24-hour_clock), the United States tends to use a  [12-hour clock](https://en.wikipedia.org/wiki/12-hour_clock). Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Just as “12:00 AM” in 12-hour format would be “00:00” in 24-hour format, so would “12:01 AM” through “12:59 AM” be “00:01” through “00:59”, respectively.

In a file called  `working.py`, implement a function called  `convert`  that expects a  `str`  in either of the 12-hour formats below and returns the corresponding  `str`  in 24-hour format (i.e.,  `9:00 to 17:00`). Expect that  `AM`  and  `PM`  will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

-   `9:00 AM to 5:00 PM`
-   `9 AM to 5 PM`

Raise a  `ValueError`  instead if the input to  `convert`  is not in either of those formats or if either time is invalid (e.g.,  `12:60 AM`,  `13:00 PM`, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g.,  `5:00 PM to 9:00 AM`).
