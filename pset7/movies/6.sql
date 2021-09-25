/* write a SQL query to determine the average rating of all movies released in 2012.
   Your query should output a table with a single column and a single row (not including the header) containing the average rating. */

SELECT AVG(rating)
FROM ratings AS r
INNER JOIN movies AS m
ON m.id = r.movie_id AND m.year = 2012;
