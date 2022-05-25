# [Birthdays](https://cs50.harvard.edu/x/2022/labs/9/#lab-9-birthdays)
Create a web application to keep track of friends’ birthdays.

![screenshot of birthdays website](https://cs50.harvard.edu/x/2022/labs/9/birthdays.png)
## Implementation Details
Complete the implementation of a web application to let users store and keep track of birthdays.

-   When the  `/`  route is requested via  `GET`, your web application should display, in a table, all of the people in your database along with their birthdays.
    -   First, in  `app.py`, add logic in your  `GET`  request handling to query the  `birthdays.db`  database for all birthdays. Pass all of that data to your  `index.html`  template.
    -   Then, in  `index.html`, add logic to render each birthday as a row in the table. Each row should have two columns: one column for the person’s name and another column for the person’s birthday.
-   When the  `/`  route is requested via  `POST`, your web application should add a new birthday to your database and then re-render the index page.
    -   First, in  `index.html`, add an HTML form. The form should let users type in a name, a birthday month, and a birthday day. Be sure the form submits to  `/`  (its “action”) with a method of  `post`.
    -   Then, in  `app.py`, add logic in your  `POST`  request handling to  `INSERT`  a new row into the  `birthdays`  table based on the data supplied by the user.
