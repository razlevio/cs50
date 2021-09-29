

SELECT DISTINCT(name) FROM people
INNER JOIN stars ON stars.person_id = people.id
INNER JOIN movies ON movies.id = stars.movie_id
WHERE movies.id IN
    (
        SELECT movie_id FROM movies
        INNER JOIN stars ON stars.movie_id = movies.id
        INNER JOIN people ON people.id = stars.person_id
        WHERE people.name = 'Kevin Bacon' AND people.birth = 1958
    )
    AND people.name <> 'Kevin Bacon'