-- script that lists all genres and there counts
SELECT tg.name as genre,
       COUNT(tsg.show_id) as number_of_shows
FROM tv_genres tg  LEFT JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
GROUP BY tg.name
HAVING COUNT(tsg.show_id) > 0
ORDER BY number_of_shows DESC;