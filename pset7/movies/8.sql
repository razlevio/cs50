/*In 8.sql, write a SQL query to list the names of all people who starred in Toy Story.
Your query should output a table with a single column for the name of each person.
You may assume that there is only one movie in the database with the title Toy Story.*/

SELECT p.name
    FROM people AS p
    INNER JOIN stars AS s
    ON p.id = s.person_id
    INNER JOIN movies AS m
    ON m.title = 'Toy Story' AND m.id = s.movie_id;
