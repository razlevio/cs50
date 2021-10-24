/*write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.
Your query should output a table with a single column for the title of each movie.
You may assume that there is only one person in the database with the name Johnny Depp.
You may assume that there is only one person in the database with the name Helena Bonham Carter.*/

SELECT DISTINCT m.title
    FROM movies AS m
    WHERE m.id IN
    (
        SELECT s.movie_id FROM stars AS s WHERE s.person_id = (SELECT p.id FROM people AS p WHERE p.name = 'Helena Bonham Carter')
    AND
        s.movie_id IN (SELECT s.movie_id FROM stars AS s WHERE s.person_id = (SELECT p.id FROM people AS p WHERE p.name = 'Johnny Depp'))
    )

