/*write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
Your query should output a table with a single column for the title of each movie.
You may assume that there is only one person in the database with the name Chadwick Boseman.*/

SELECT m.title
    FROM movies AS m
    INNER JOIN stars AS s
    ON m.id = s.movie_id
    INNER JOIN people AS p
    ON s.person_id = p.id AND p.name = 'Chadwick Boseman'
    INNER JOIN ratings AS r
    ON m.id = r.movie_id
    ORDER BY r.rating DESC
    LIMIT 5;