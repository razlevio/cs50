/*write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.
Your query should output a table with a single column for the name of each person.
If a person directed more than one movie that received a rating of at least 9.0, they should only appear in your results once.*/

SELECT DISTINCT p.name
    FROM people AS p
    INNER JOIN ratings AS r
    ON r.rating >= 9.0
    INNER JOIN directors AS d
    ON r.movie_id = d.movie_id AND p.id = d.person_id;